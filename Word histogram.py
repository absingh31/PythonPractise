from pprint import pprint
import sys
s=input()
s=s.lower()
coll={}
inv={}
dig=['1','2','3','4','5','6','7','8','9','0']
for i in s:
    if i in dig:
        print("Invalid input")
        sys.exit(0)
for i in s:
    c=0
    for j in s[s.index(i):]:
        if (j==i):
            c+=1
            s.replace(j,'')
    d={i:c}
    coll.update(d)
for i in list(coll.values()):
    l=[]
    for j in list(coll.items()):
        if j[1]==i:
            l.append(j[0])
    l.sort()
    d={i:l}
    inv.update(d)
pprint(coll)
print(inv)
            
