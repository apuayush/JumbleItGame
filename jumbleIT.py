import random
k=[]
def perm(s,t):
    if len(s)==0:
        k.append(t)
        return
    for i in range(len(s)):
        perm(s[0:i]+s[i+1:],t+s[i])

def choose(s):
    perm(s,'')
    return(random.choice(k))
