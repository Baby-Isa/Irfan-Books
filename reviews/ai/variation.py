import re,statistics as st,subprocess,glob,math,collections
def git(rev,path): return subprocess.run(["git","show",f"{rev}:{path}"],capture_output=True,text=True).stdout
def chprose(s):
    s=re.sub(r"^---.*?---\n","",s,flags=re.S); s=re.sub(r"::::? \{\.point\}.*?\n::::\n","",s,flags=re.S)
    s=re.sub(r"<!--.*?-->","",s,flags=re.S); s=re.sub(r"^:::.*?^:::\s*$","",s,flags=re.S|re.M)
    s=re.sub(r"\^\[[^\]]*\]","",s); s=re.sub(r"\s*\[@[^\]]*\]","",s); s=re.sub(r"^#.*$","",s,flags=re.M); s=re.sub(r"^\|.*$","",s,flags=re.M)
    s=re.sub(r"\[([^\]]*)\]\{[^}]*\}",r"\1",s); s=s.replace("*","")
    return [re.sub(r"\s+"," ",p).strip() for p in s.split("\n\n") if len(p.split())>15]
def human(path,pages):
    s=open(path).read(); out=[]
    for pg in pages:
        i=s.index(f"[p. {pg}]"); j=s.find("[p. ",i+8); j=s.find("[p. ",j+8)
        t=s[i:j]; t=re.sub(r"\[p\. \d+\]","",t).replace("ﬁ","fi").replace("ﬂ","fl")
        out+= [re.sub(r"\s+"," ",p).strip() for p in re.split(r"\n\s*\n",t) if len(p.split())>15]
    return out
SPLIT=re.compile(r"(?<=[.!?])[\"”’)]?\s+(?=[A-Z“\"ʿ‘(])")
def sents(paras):
    out=[]
    for pi,p in enumerate(paras):
        ss=[x for x in SPLIT.split(p) if len(x.split())>=2]
        for si,x in enumerate(ss): out.append((pi,si,len(ss),x))
    return out
FIRST=lambda x: re.sub(r"[^\w']","",x.split()[0]).lower() if x.split() else ""
def feats(paras):
    S=sents(paras); L=[len(x.split()) for *_,x in S]
    d=[abs(a-b) for a,b in zip(L,L[1:])]
    m=st.mean(L); sd=st.pstdev(L)
    ac=sum((a-m)*(b-m) for a,b in zip(L,L[1:]))/((len(L)-1)*sd*sd) if sd else 0
    commas=[x.count(",") for *_,x in S]
    firsts=collections.Counter(FIRST(x) for *_,x in S)
    the_share=firsts["the"]/len(S)
    top5=sum(c for _,c in firsts.most_common(5))/len(S)
    # paragraph shape: length of last sentence vs paragraph mean
    last_short=sum(1 for pi,si,n,x in S if si==n-1 and n>1 and len(x.split())<0.7*m)/max(1,len(set(p for p,*_ in S)))
    # rhythm: proportion of consecutive pairs both within 25% of each other (monotone)
    mono=sum(1 for a,b in zip(L,L[1:]) if abs(a-b)<=0.25*max(a,b))/len(d)
    # band: share of sentences 12-24 words
    band=sum(1 for x in L if 12<=x<=24)/len(L)
    semi=sum(x.count(";") for *_,x in S)/len(S)
    colon=sum(x.count(":") for *_,x in S)/len(S)
    return dict(n=len(S),mean=round(m,1),sd=round(sd,1),cv=round(sd/m,2),short=round(sum(1 for x in L if x<=8)/len(L)*100),long=round(sum(1 for x in L if x>=35)/len(L)*100),
                band=round(band*100),mono=round(mono*100),meandiff=round(st.mean(d),1),lag1=round(ac,2),commas=round(st.mean(commas),2),zero_comma=round(sum(1 for c in commas if c==0)/len(S)*100),
                the=round(the_share*100),top5=round(top5*100),semi=round(semi,2),colon=round(colon,2),lastshort=round(last_short*100))
G={}
G["HUMAN Mutahhari (Light)"]=human("sources/extracts/light.md",[44,57,63,89,95])
G["HUMAN Tabatabaʾi (Kernel)"]=human("sources/extracts/kernel.md",[40,60,62,72])
G["HUMAN Khomeini (Forty Hadith)"]=human("sources/extracts/forty_hadith.md",[89,249,250,515])
G["HUMAN Amuli (Inner Secrets)"]=human("sources/extracts/inner_secrets.md",[108,109,115,195])
G["AI raw drafts Ch 8-12"]=sum([chprose(git("6ebea1e",f"book2/chapters/{f}.md")) for f in ["08-stages-of-the-journey","09-polishing-setting-out","10-emptying-five-disciplines","12-passing-away"]],[])
G["Ch 1 first draft (7 Oct)"]=chprose(git("ce4529b","book2/chapters/01-seeking-not-powers.md"))
G["Ch 1 approved (12 Oct)"]=chprose(git("32e44c9","book2/chapters/01-seeking-not-powers.md"))
G["Ch 1 today"]=chprose(open("book2/chapters/01-seeking-not-powers.md").read())
G["Ch 3 today (GPTZero: mixed)"]=chprose(open("book2/chapters/03-you-already-know-these-words.md").read())
G["Part Three today"]=sum([chprose(open(f).read()) for f in sorted(glob.glob("book2/chapters/0[89]-*.md")+glob.glob("book2/chapters/1[0-2]-*.md"))],[])
G["Prologue"]=chprose(open("book2/chapters/00-prologue.md").read())
G["Anchor (Linus+AI)"]=[p for p in open("reviews/ai/anchor.txt").read().split("\n\n") if p.strip()]
rows=[(k,feats(v)) for k,v in G.items()]
keys=list(rows[0][1])
print("group".ljust(32)+"".join(k[:8].rjust(9) for k in keys))
for k,f in rows: print(k[:31].ljust(32)+"".join(str(f[x]).rjust(9) for x in keys))
print()
ABS=re.compile(r"\b\w+(tion|ness|ment|ity|ance|ence|ism)s?\b",re.I)
for k,v in G.items():
    t=" ".join(v); w=len(t.split())
    q=sum(len(m.split()) for m in re.findall(r'"([^"]{3,})"',t))+sum(len(m.split()) for m in re.findall(r'“([^”]{3,})”',t))
    caps=len(re.findall(r"(?<![.!?]\s)(?<!^)\b[A-Zʿ][a-zʾʿ]+",t))
    print(k[:31].ljust(32),"quoted words %3d%%"%(100*q/w),"  abstract nouns/100w %4.1f"%(100*len(ABS.findall(t))/w),"  capitalised names/100w %4.1f"%(100*caps/w))
