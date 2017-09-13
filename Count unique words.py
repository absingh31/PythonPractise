from pprint import pprint
import sys
s=input()
s=s.lower()
fin={}
spl=['!','?','.',',',';',':']
dig=['1','2','3','4','5','6','7','8','9','0']
for i in range(len(s)-1):
    if s[i] in spl and s[i+1] in spl:
        print("Invalid input")
        sys.exit(0)
for i in s:
    if i in dig:
        print("Invalid input")
        sys.exit(0)
a=s.split()
b=[]
for i in a:
    if i[0] in spl:
        print("Invalid input")
        sys.exit(0)
for i in a:
    s1=''
    for j in i:
        if j not in spl:
            s1+=j       
    b.append(s1)
for i in b:
    d={i:b.count(i)}
    fin.update(d)
pprint(fin)
