def calcTime(x,y,z):
    return(int(x/50)+int(3*y/100)+int(z/100))
x=int(input())
y=int(input())
z=int(input())
m=int(input())
if (x>=0 and y>=0 and z>=0 and m>=0):
    a=calcTime(x,y,z)
    ha=6
    b=calcTime(x,z,y)
    b+=m+a
    hb=6
    while a>=60:
        ha+=1
        a-=60
    while b>=60:
        hb+=1
        b-=60
    print(ha,a)
    print(hb,b)
else:
    print("Invalid input")
