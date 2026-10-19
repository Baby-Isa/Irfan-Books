import re,sys
AUX=set("is are was were be been being has have had does do did can could will would may might must shall should am".split())
SUBJ=set("i we you he she it they this that there who which".split())
def body(s):
    s=re.sub(r"^---.*?---\n","",s,flags=re.S); s=re.sub(r"::::? \{\.point\}.*?\n::::\n","",s,flags=re.S)
    s=re.sub(r"<!--.*?-->","",s,flags=re.S); s=re.sub(r"^(:::|#|\|).*$","",s,flags=re.M); s=re.sub(r"\[@[^\]]*\]","",s)
    return s.replace("*","")
def tails(text):
    out=[]
    for para in body(text).split("\n\n"):
        para=re.sub(r"\s+"," ",para).strip()
        for sen in re.split(r"(?<=[.!?])[\"”]?\s+(?=[A-Z“\"ʿ])",para):
            if sen.count('"')%2 or len(sen.split())<10: continue
            core=re.sub(r'"[^"]*"','Q',sen)
            if "," not in core: continue
            tail=core.rsplit(",",1)[1].strip(" .")
            w=tail.lower().split()
            if len(w)<3 or w[0] in ("and","or","but","so","since","because","which","who","whose","whereas","while","as","when","where","until","though","although","if","for","yet","nor") : continue
            if w[0]=="q": continue
            if any(x in AUX for x in w) or (w[0] in SUBJ): continue
            if re.search(r"\b\w+(s|ed)\b",tail) and w[0] in SUBJ: continue
            out.append(sen)
    return out
tot=0
for f in sys.argv[1:]:
    t=tails(open(f).read()); tot+=len(t); print(f.split("/")[-1][:30].ljust(32),len(t))
    if "-v" in sys.argv[1:2]: pass
print("total",tot)
