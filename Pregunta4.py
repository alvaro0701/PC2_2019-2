import os
os.system("cls")
import random

while True:
    x=int(input("ingrese numero entre 2 y 5:"))
    if x>=2 and x<=5:
        break
    else:
        print("intente de nuevo")
cona=0
conb=0
conc=0
cond=0
cone=0
conf=0
conh=0
coni=0
con=0
if x==2:
  for i in range(1):
    a= random.randint(1,100)
    if a%2==0:
        cona+=1
    b= random.randint(1,100)
    if b%2==0:
        conb+=1
    c= random.randint(1,100)
    if c%2==0:
        conc+=1
    d= random.randint(1,100)
    if d%2==0:
        cond+=1
    print(a,b)
    print(c,d)

if x==3:
  for i in range(1):
    a= random.randint(1,100)
    if a%2==0:
        cona+=1
    b= random.randint(1,100)
    if b%2==0:
        conb+=1
    c= random.randint(1,100)
    if c%2==0:
        conc+=1
    d= random.randint(1,100)
    if d%2==0:
        cond+=1
    e= random.randint(1,100)
    if e%2==0:
        cone+=1
    f= random.randint(1,100)
    if f%2==0:
        conf+=1
    g= random.randint(1,100)
    if g%2==0:
        cong+=1
    h= random.randint(1,100)
    if h%2==0:
        conh+=1
    i= random.randint(1,100)
    if i%2==0:
        coni+=1
    print(a,b,c)
    print(d,e,f)
    print(g,h,i)
con=cona+conb+conc+cond+cone+conf+conh+coni
print("Cantidad de numeros pares:",con)
if x==4:
  for i in range(1):
    a= random.randint(1,100)
    b= random.randint(1,100)
    c= random.randint(1,100)
    d= random.randint(1,100)
    e= random.randint(1,100)
    f= random.randint(1,100)
    g= random.randint(1,100)
    h= random.randint(1,100)
    i= random.randint(1,100)
    j= random.randint(1,100)
    k= random.randint(1,100)
    m= random.randint(1,100)
    n= random.randint(1,100)
    o= random.randint(1,100)
    p= random.randint(1,100)
    q= random.randint(1,100)

    print(a,b,c,n)
    print(d,e,f,o)
    print(g,h,i,p)
    print(j,k,m,q)
if x==5:
  for i in range(1):
    a= random.randint(1,100)
    b= random.randint(1,100)
    c= random.randint(1,100)
    d= random.randint(1,100)
    e= random.randint(1,100)
    f= random.randint(1,100)
    g= random.randint(1,100)
    h= random.randint(1,100)
    i= random.randint(1,100)
    j= random.randint(1,100)
    k= random.randint(1,100)
    m= random.randint(1,100)
    n= random.randint(1,100)
    o= random.randint(1,100)
    p= random.randint(1,100)
    q= random.randint(1,100)
    r= random.randint(1,100)
    s= random.randint(1,100)
    t= random.randint(1,100)
    u= random.randint(1,100)
    v= random.randint(1,100)
    w= random.randint(1,100)
    x= random.randint(1,100)
    y= random.randint(1,100)
    z= random.randint(1,100)
    print(a,b,c,q,r)
    print(d,e,f,s,t)
    print(g,h,i,u,v)
    print(j,k,m,w,x)
    print(n,o,p,y,z)
