import re,subprocess,json,sys,glob,math,statistics as st
sys.path.insert(0,"/tmp/claude-0/-home-user-Irfan-Books/13b18659-63a4-543c-a421-93e40cbc78c2/scratchpad/det")
from det import score
import numpy as np
def git(rev,path): return subprocess.run(["git","show",f"{rev}:{path}"],capture_output=True,text=True).stdout
def clean_ch(s):
    s=re.sub(r"^---.*?---\n","",s,flags=re.S); s=re.sub(r"::::? \{\.point\}.*?\n::::\n","",s,flags=re.S)
    s=re.sub(r"<!--.*?-->","",s,flags=re.S); s=re.sub(r"^:::.*?^:::\s*$","",s,flags=re.S|re.M)
    s=re.sub(r"\[@[^\]]*\]","",s); s=re.sub(r"^#.*$","",s,flags=re.M); s=re.sub(r"^\|.*$","",s,flags=re.M)
    return [re.sub(r"\s+"," ",p).strip() for p in s.replace("*","").split("\n\n") if len(p.split())>35]
def passages(ps,n=2,w=230):
    out=[]
    for k in range(n):
        start=len(ps)*(k+1)//(n+1); acc=[];c=0
        for p in ps[start:]:
            acc.append(p); c+=len(p.split())
            if c>=w: break
        out.append(" ".join(acc))
    return out
def human(path,pages):
    s=open(path).read(); out=[]
    for pg in pages:
        i=s.index(f"[p. {pg}]"); t=s[i:i+5000]
        t=re.sub(r"\[p\. \d+\]","",t).replace("ﬁ","fi").replace("ﬂ","fl"); t=re.sub(r"(?<=[a-z])\d+","",t)
        t=re.sub(r"\s*\n\s*"," ",t); words=t.split(); out.append(" ".join(words[30:30+240]))
    return out
R={"human":[], "ai_draft":[], "now":{}, "before":{}}
for path,pages in [("sources/extracts/light.md",[30,60,95]),("sources/extracts/kernel.md",[40,62,76]),("sources/extracts/forty_hadith.md",[89,249,300]),("sources/extracts/inner_secrets.md",[108,150,195])]:
    R["human"]+= [score(t) for t in human(path,pages)]
for f in ["08-stages-of-the-journey","09-polishing-setting-out","10-emptying-five-disciplines","12-passing-away"]:
    R["ai_draft"]+= [score(t) for t in passages(clean_ch(git("6ebea1e",f"book2/chapters/{f}.md")))]
R["ai_draft"]+= [score(t) for t in passages(clean_ch(git("34b491b","book2/chapters/11-adornment-love.md")))]
R["anchor"]=score(open("reviews/ai/anchor.txt").read())
for f in sorted(glob.glob("book2/chapters/*.md")):
    n=f.split("/")[-1][:2]
    R["now"][n]=[score(t) for t in passages(clean_ch(open(f).read()))]
    old={"08":("1e74648","08-stages-of-the-journey"),"09":("1e74648","09-polishing-setting-out"),"10":("1e74648","10-emptying-five-disciplines"),"11":("1e74648","11-adorning-love"),"12":("1e74648","12-passing-away")}
    rev,name=old.get(n,("4f0e1f6",f.split("/")[-1][:-3]))
    R["before"][n]=[score(t) for t in passages(clean_ch(git(rev,f"book2/chapters/{name}.md")))]
json.dump(R,open("/tmp/claude-0/-home-user-Irfan-Books/13b18659-63a4-543c-a421-93e40cbc78c2/scratchpad/det/results.json","w"),indent=1)
print("done")
