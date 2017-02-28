import random
import jumbleIT
score=0
tv_show=['breaking bad','game of thrones','bleach','Mr Robot','The Simpson','fullmetal alchemist brotherhood','avatar','house md','friends','sherlock','the west wing','the walking dead','family guy','modern family','agents of shield','supernaturals','gotham']
def calc(t1,a):
    if t1.strip()==a.strip():
        return 1
    return 0
for i in random.sample(tv_show,5):
    t1=''
    for j in i.split():
        t1+=jumbleIT.choose(j)+' '
        jumbleIT.k=[]
    print t1,(40-len(t1))*' ','-',10*' ',
    a=raw_input()
    score+=calc(i,a)
print(score)
