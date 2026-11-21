#!/usr/bin/env python3
"""Audit the Materiales_UBA PDF corpus: text layer, scan status, OCR quality,
layout, encryption, duplicates. Writes audit.json next to this script."""
import hashlib, json, os, re, sys, unicodedata
import fitz  # pymupdf

ROOT = sys.argv[1] if __name__ == "__main__" else ""
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "auditoria_corpus.json")
SKIP = {"TPs_1", "TPs_2", "__pycache__"}

ES = set("de la que el en y a los se del las un por con no una su para es al lo como más pero sus le ya o este sí porque esta entre cuando muy sin sobre también me hasta hay donde quien desde todo nos durante todos uno les ni contra otros ese eso ante ellos e esto mí antes algunos qué unos yo otro otras otra él tanto esa estos mucho quienes nada muchos cual poco ella estar estas algunas algo nosotros".split())
EN = set("the of and to in a is that for it as was with be by on not he this are or his from at which but have an they you were their one all we can her has there been if more when will would who so no".split())

def norm(s):
    return unicodedata.normalize("NFC", s)

def text_quality(txt):
    toks = re.findall(r"[^\W\d_]+", txt.lower())
    if len(toks) < 30:
        return None
    es = sum(t in ES for t in toks) / len(toks)
    en = sum(t in EN for t in toks) / len(toks)
    # junk: single letters that are not real one-letter words, mixed digit/letter tokens
    single = sum(1 for t in toks if len(t) == 1 and t not in {"a", "y", "o", "e", "u"}) / len(toks)
    mixed = len(re.findall(r"\b(?=\w*\d)(?=\w*[^\W\d_])\w+\b", txt)) / max(1, len(toks))
    nonprint = sum(1 for c in txt if not (c.isalnum() or c.isspace() or c in ".,;:¡!¿?()[]«»\"'“”‘’-–—/%°ºª§$&*+=<>…|_#@")) / max(1, len(txt))
    lang = "es" if es >= en else "en"
    func = max(es, en)
    # crude score 0-100: function-word ratio near normal (~.35-.5), little junk
    score = min(1, func / 0.33) * 100 - single * 300 - mixed * 200 - nonprint * 300
    return dict(lang=lang, func=round(func, 3), single=round(single, 3),
                mixed=round(mixed, 3), nonprint=round(nonprint, 4),
                score=round(max(0, min(100, score)), 1))

def audit(path):
    r = dict(path=os.path.relpath(path, ROOT), bytes=os.path.getsize(path))
    with open(path, "rb") as f:
        r["md5"] = hashlib.md5(f.read()).hexdigest()
    try:
        doc = fitz.open(path)
    except Exception as e:
        r["error"] = f"open: {e}"
        return r
    r["encrypted"] = doc.is_encrypted
    if doc.needs_pass:
        r["error"] = "needs password"
        return r
    r["pages"] = doc.page_count
    md = doc.metadata or {}
    r["producer"] = (md.get("producer") or "")[:60]
    r["creator"] = (md.get("creator") or "")[:60]
    r["title_meta"] = (md.get("title") or "")[:80]
    r["page_labels"] = bool(doc.get_page_labels())
    per = []
    fulltext = []
    fonts = set()
    for p in doc:
        w, h = p.rect.width, p.rect.height
        txt = p.get_text("text")
        fulltext.append(txt)
        area = w * h
        img_cov = 0.0
        try:
            for info in p.get_image_info():
                x0, y0, x1, y1 = info["bbox"]
                img_cov += max(0, (x1 - x0)) * max(0, (y1 - y0))
        except Exception:
            pass
        img_cov = min(1.0, img_cov / area) if area else 0
        invisible = 0
        total_spans = 0
        try:
            for b in p.get_texttrace():
                total_spans += 1
                if b.get("type") == 3 or b.get("opacity", 1) == 0:
                    invisible += 1
        except Exception:
            pass
        for fnt in p.get_fonts():
            fonts.add(fnt[3])
        per.append(dict(chars=len(txt.strip()), img=round(img_cov, 2),
                        land=w > h * 1.15, rot=p.rotation,
                        invis=(invisible / total_spans) if total_spans else 0))
    n = len(per)
    r["pages_with_text"] = sum(1 for x in per if x["chars"] > 200)
    r["pages_scanned"] = sum(1 for x in per if x["img"] > 0.7)
    r["pages_landscape"] = sum(1 for x in per if x["land"])
    r["pages_rotated"] = sum(1 for x in per if x["rot"])
    r["pages_blank"] = sum(1 for x in per if x["chars"] < 20 and x["img"] < 0.05)
    r["chars_per_page"] = round(sum(x["chars"] for x in per) / n) if n else 0
    r["invisible_text"] = round(sum(x["invis"] for x in per) / n, 2) if n else 0
    r["glyphless"] = any("GlyphLess" in f for f in fonts)
    t = norm("\n".join(fulltext))
    r["quality"] = text_quality(t)
    r["hyphen_breaks"] = len(re.findall(r"[^\W\d_]-\n[^\W\d_]", t))
    # classify
    scanned = r["pages_scanned"] >= max(1, 0.6 * n)
    has_text = r["pages_with_text"] >= 0.6 * n
    if not scanned and has_text:
        kind = "digital"
    elif scanned and not has_text:
        kind = "scan-no-text"
    elif scanned and has_text:
        kind = "scan-with-ocr"
    else:
        kind = "mixed"
    r["kind"] = kind
    r["two_up"] = scanned and r["pages_landscape"] >= 0.6 * n
    r["first_text"] = re.sub(r"\s+", " ", t[:400]).strip()
    return r

def main():
    files = []
    for d in sorted(os.listdir(ROOT)):
        full = os.path.join(ROOT, d)
        if d in SKIP or not os.path.isdir(full):
            continue
        for fn in sorted(os.listdir(full)):
            if fn.lower().endswith(".pdf"):
                files.append(os.path.join(full, fn))
    out = []
    for i, f in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {os.path.relpath(f, ROOT)}", file=sys.stderr, flush=True)
        out.append(audit(f))
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print("wrote", OUT)

if __name__ == "__main__":
    main()
