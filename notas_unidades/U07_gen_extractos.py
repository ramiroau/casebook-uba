import fitz, re, sys
import os
_RAIZ=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAT=os.path.join(os.path.dirname(_RAIZ),"Materiales_UBA")+"/"
EXT=os.path.join(_RAIZ,"extractos")+"/"
def clean(t): 
    t=t.replace("\xa0"," ")
    return re.sub(r" {2,}"," ",t).strip()

def emit(out, lines):
    # lines: list of (text, newpar)
    buf=[]
    for t,newpar in lines:
        if not t: continue
        if newpar and buf and buf[-1]!="":
            buf.append("")
        if buf and buf[-1] and (buf[-1].endswith("‐") or (buf[-1].endswith("-") and t[:1].isdigit())):
            buf[-1]=buf[-1]+t
        else:
            buf.append(t)
    out.extend(buf)

def jgb():
    src="Unidad7/1_González Bertomeu_2008_Notas sobre federalismo2.pdf"
    d=fitz.open(MAT+src)
    out=["# fuente: "+src,"# modo: texto","# generado: 2026-11-20 (PyMuPDF, sólo cuerpo de 11,3 pt)",
         "# criterio: re-extracción del PDF digital con PyMuPDF. Se conservan sólo los renglones del cuerpo (11,3 pt);",
         "#   se descartan notas al pie (9,4 pt), llamadas de nota (superíndices), números de página, el cuadro de PDF p. 35",
         "#   y su leyenda. Punto y aparte reconstruido por el espacio vertical entre renglones. El texto de corpus/texto/jgb2008.txt",
         "#   (pdftotext -layout) intercala las notas en el cuerpo.",""]
    for i,pg in enumerate(d):
        out.append(f"[[PDF p. {i+1}]]")
        rows=[]
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines",[]):
                sp=[s for s in l["spans"] if s["text"].strip()]
                if not sp: continue
                body=[s for s in sp if abs(s["size"]-11.3)<0.3 and not (s["flags"]&1)]
                if not body: continue
                if l["bbox"][1]>725: continue  # número de página
                txt=clean("".join(s["text"] for s in l["spans"] if abs(s["size"]-11.3)<0.3 and not (s["flags"]&1)))
                if not txt: continue
                rows.append((l["bbox"][1],l["bbox"][0],txt))
        rows.sort()
        lines=[];prev=None
        for y,x,t in rows:
            newpar = prev is not None and (y-prev)>24
            lines.append((t,newpar)); prev=y
        emit(out,lines); out.append("")
    open(EXT+"jgb2008.txt","w").write("\n".join(out)+"\n")

def mendez():
    src="Unidad7/2_Méndez Montenegro_Vitaliani_2021_Haz lo que yo digo, pero no lo que yo hago.pdf"
    d=fitz.open(MAT+src)
    out=["# fuente: "+src,"# modo: texto","# generado: 2026-11-20 (PyMuPDF, por columnas)",
         "# criterio: re-extracción del PDF digital con PyMuPDF, columna izquierda y luego derecha; sólo renglones de 9,5 pt",
         "#   (cuerpo); se descartan notas al pie (8 pt), cabezales y pies (8 y 10 pt) y el título de PDF p. 1. Se quitan las",
         "#   llamadas de nota «(N)». Punto y aparte por sangría de primera línea y por títulos. El texto de",
         "#   corpus/texto/mendez2021.txt (pdftotext -layout) intercala las dos columnas renglón por renglón.",""]
    for i,pg in enumerate(d):
        out.append(f"[[PDF p. {i+1}]]")
        rows=[]
        for b in pg.get_text("dict")["blocks"]:
            for l in b.get("lines",[]):
                sp=[s for s in l["spans"] if s["text"].strip()]
                if not sp or abs(sp[0]["size"]-9.5)>0.2: continue
                txt=clean("".join(s["text"] for s in l["spans"]))
                txt=re.sub(r"\s?\(\d{1,2}\)","",txt).strip()
                col=0 if l["bbox"][0]<240 else 1
                isb=all("Bold" in s["font"] or "Italic" in s["font"] for s in sp) and len(txt)<60
                head=isb and re.match(r"^(I|II|III|IV|V|VI)[\.\d]*\.? ",txt) is not None
                rows.append((col,l["bbox"][1],l["bbox"][0],txt,(isb,head)))
        rows.sort()
        lines=[];prevbold=False
        for col,y,x,t,(isb,head) in rows:
            margin=43 if col==0 else 247
            newpar = head or (prevbold and not isb) or ((x-margin)>=5 and not (prevbold and isb))
            bold=isb
            if not t: continue
            lines.append((t,newpar)); prevbold=bold
        emit(out,lines); out.append("")
    open(EXT+"mendez2021.txt","w").write("\n".join(out)+"\n")
jgb(); mendez()
