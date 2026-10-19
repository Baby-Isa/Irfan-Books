import re,sys,statistics as st
def body(path):
    s=open(path).read()
    s=re.sub(r"^---.*?---\n","",s,flags=re.S)
    s=re.sub(r"::::? \{\.point\}.*?\n::::\n","",s,flags=re.S)
    s=re.sub(r"<!--.*?-->","",s,flags=re.S)
    s=re.sub(r"^:::.*$","",s,flags=re.M)
    s=re.sub(r"\[@[^\]]*\]","",s)
    s=re.sub(r"^#.*$","",s,flags=re.M)
    s=re.sub(r"^\|.*$","",s,flags=re.M)
    return s
def sents(t):
    t=re.sub(r"\s+"," ",t)
    return [x for x in re.split(r"(?<=[.!?])[\"”’]?\s+(?=[A-Z“\"ʿ*])",t) if len(x.split())>1]
pat={
 "not X but/rather Y": r"\b(?:not|isn't|is not|was not|wasn't)\b[^.;]{1,60}?\b(?:but|rather|instead)\b",
 "It is not X. It is Y": r"\b(?:is|was) not [^.]{1,60}\.\s+(?:It|This|That) (?:is|was)\b",
 "triplet list": r"\b\w+(?:\s\w+){0,3}, \w+(?:\s\w+){0,3},? (?:and|or) \w+",
 "therefore/thus/so": r"\b(?:therefore|thus|hence)\b",
 "signpost 'This chapter'": r"\bThis (?:chapter|section|book)\b",
 "whereas": r"\bwhereas\b",
 "stock AI words": r"\b(?:profound|deeply|truly|tapestry|delve|nuanced|rich|vital|crucial|journey|realm|landscape|testament|resonate)\w*\b",
}
def run(path):
    t=body(path); w=len(t.split()); S=sents(t); L=[len(x.split()) for x in S]
    paras=[p for p in t.split("\n\n") if len(p.split())>8]
    endshort=sum(1 for p in paras if len(sents(p)[-1].split())<=8) if paras else 0
    r={"words":w,"sent CV":round(st.pstdev(L)/st.mean(L),2) if L else 0,
       "short sents<=6 %":round(100*sum(1 for x in L if x<=6)/len(L),1),
       "para ends short %":round(100*endshort/max(1,len(paras)),1)}
    for k,v in pat.items(): r[k]=round(1000*len(re.findall(v,t,flags=re.I))/max(w,1),1)
    return r
rows=[(p.split("/")[-1][:22],run(p)) for p in sys.argv[1:]]
keys=list(rows[0][1].keys())
print("file".ljust(24)+"".join(k[:12].rjust(13) for k in keys))
for n,r in rows: print(n.ljust(24)+"".join(str(r[k]).rjust(13) for k in keys))
