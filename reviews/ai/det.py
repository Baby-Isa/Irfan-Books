import json, regex as re, numpy as np, onnxruntime as ort, sys, statistics as st
from functools import lru_cache
D=__file__.rsplit("/",1)[0]
enc=json.load(open(D+"/encoder.json")); bpe=[tuple(l.split()) for l in open(D+"/vocab.bpe",encoding="utf-8").read().split("\n")[1:-1]]
ranks=dict(zip(bpe,range(len(bpe))))
def b2u():
    bs=list(range(ord("!"),ord("~")+1))+list(range(ord("¡"),ord("¬")+1))+list(range(ord("®"),ord("ÿ")+1)); cs=bs[:]; n=0
    for b in range(256):
        if b not in bs: bs.append(b); cs.append(256+n); n+=1
    return dict(zip(bs,map(chr,cs)))
B2U=b2u(); PAT=re.compile(r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+""")
@lru_cache(None)
def bpe_tok(t):
    w=tuple(t)
    while len(w)>1:
        pairs=set(zip(w,w[1:])); p=min(pairs,key=lambda x:ranks.get(x,1e10))
        if p not in ranks: break
        a,b=p; nw=[];i=0
        while i<len(w):
            if i<len(w)-1 and w[i]==a and w[i+1]==b: nw.append(a+b); i+=2
            else: nw.append(w[i]); i+=1
        w=tuple(nw)
    return w
def encode(text):
    ids=[]
    for t in PAT.findall(text):
        t="".join(B2U[b] for b in t.encode("utf-8"))
        ids+= [enc[x] for x in bpe_tok(t) if x in enc]
    return ids
sess=ort.InferenceSession(D+"/gpt2.onnx")
def score(text):
    ids=encode(text)[:1000]
    x=np.array([[ids]],dtype=np.int64)
    logits=sess.run(["output1"],{"input1":x})[0][0,0]   # T x V
    lp=logits-logits.max(-1,keepdims=True); lp=lp-np.log(np.exp(lp).sum(-1,keepdims=True))
    tgt=np.array(ids[1:]); l=lp[:-1]
    tok_lp=l[np.arange(len(tgt)),tgt]
    rank=(l>tok_lp[:,None]).sum(-1)
    ppl=float(np.exp(-tok_lp.mean()))
    # per-sentence perplexity for burstiness
    return {"tokens":len(ids),"ppl":round(ppl,1),"top10":round(float((rank<10).mean()),3),"top1":round(float((rank<1).mean()),3),"beyond1000":round(float((rank>=1000).mean()),3),"lp_std":round(float(tok_lp.std()),2)}
if __name__=="__main__":
    print(score(open(sys.argv[1]).read()))
