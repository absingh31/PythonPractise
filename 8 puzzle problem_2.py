def ifPoss(a,b):
    if (0<a<4) and (0<b<4):
        print(a)
        print(b)
def run(r,c):
    ifPoss(r+1,c)
    ifPoss(r,c-1)
    ifPoss(r-1,c)
    ifPoss(r,c+1)
r=int(input())
if (0<r<4):
    run(r,1)
    run(r,2)
    run(r,3)
else:
    print("Invalid input")
