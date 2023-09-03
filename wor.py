import sys
import m
def check(str1,i,j,a,b,x,y,o,p,g,h,r6,c6,r7,c7,size):
    global count
    global v
    global bp
    pp=len(str1)-3
    ppp=ord(str1[0])-97
    for st in m.v[pp][ppp]:
        if st==str1:
            count+=1
            if bp==1:
                bp=0
                f.write("{")
            else:    
                f.write(",{")
            if size==3:
                c="{"+str(i)+","+str(j)+"}"+","+"{"+str(a)+","+str(b)+"}"+","+"{"+str(x)+","+str(y)+"}"
            elif size==4:
                c="{"+str(i)+","+str(j)+"}"+","+"{"+str(a)+","+str(b)+"}"+","+"{"+str(x)+","+str(y)+"}"+","+"{"+str(o)+","+str(p)+"}"              
            elif size==5:
                c="{"+str(i)+","+str(j)+"}"+","+"{"+str(a)+","+str(b)+"}"+","+"{"+str(x)+","+str(y)+"}"+","+"{"+str(o)+","+str(p)+"}"+","+"{"+str(g)+","+str(h)+"}"              
            elif size==6:
                c="{"+str(i)+","+str(j)+"}"+","+"{"+str(a)+","+str(b)+"}"+","+"{"+str(x)+","+str(y)+"}"+","+"{"+str(o)+","+str(p)+"}"+","+"{"+str(g)+","+str(h)+"}"+","+"{"+str(r6)+","+str(c6)+"}"              
            elif size==6:
                c="{"+str(i)+","+str(j)+"}"+","+"{"+str(a)+","+str(b)+"}"+","+"{"+str(x)+","+str(y)+"}"+","+"{"+str(o)+","+str(p)+"}"+","+"{"+str(g)+","+str(h)+"}"+","+"{"+str(r6)+","+str(c6)+"}"+","+"{"+str(r7)+","+str(c7)+"}"              
            f.write(c)    
            f.write("}")
            print(count,str1)
                   

def two(i,j,l):
    for n in range(-1,2):
        for m in range(-1,2):
            if(not(n==0 and m==0) and i+n>-1 and i+n<4 and j+m>-1 and j+m<4):
                a=i+n
                b=j+m
                str=""
                str=l[i][j]
                str+=l[a][b]
                three(i,j,a,b,str,l)
def three(i,j,a,b,str,l):
    for n in range(-1,2):
        for m in range(-1,2):
            if(not(n==0 and m==0) and a+n>-1 and a+n<4 and b+m>-1 and b+m<4 and not(a+n==i and b+m==j)):
                x=a+n
                y=b+m
                str1=str
                str1+=l[x][y]
                check(str1,i,j,a,b,x,y,0,0,0,0,0,0,0,0,3)
                four(i,j,a,b,x,y,str1,l)

def four(i,j,a,b,x,y,str,l):
    for n in range(-1,2):
        for m in range(-1,2):
            if(not(n==0 and m==0) and x+n>-1 and x+n<4 and y+m>-1 and y+m<4 and not(x+n==i and y+m==j) and not(x+n==a and y+m==b)):
                o=x+n
                p=y+m
                str1=str
                str1+=l[o][p]
                check(str1,i,j,a,b,x,y,o,p,0,0,0,0,0,0,4)
                five(i,j,a,b,x,y,o,p,str1,l)
def five(i,j,a,b,x,y,o,p,str,l):
    for n in range(-1,2):
        for m in range(-1,2):
            if(not(n==0 and m==0) and o+n>-1 and o+n<4 and p+m>-1 and p+m<4 and not(o+n==i and p+m==j) and not(o+n==a and p+m==b) and not(o+n==x and p+m==y)):
                g=o+n
                h=p+m
                str1=str
                str1+=l[g][h]
                check(str1,i,j,a,b,x,y,o,p,g,h,0,0,0,0,5)
                six(i,j,a,b,x,y,o,p,g,h,str1,l)
def six(i,j,a,b,x,y,o,p,g,h,str,l):
    for n in range(-1,2):
        for m in range(-1,2):
            if(not(n==0 and m==0) and g+n>-1 and g+n<4 and h+m>-1 and h+m<4 and not(g+n==i and h+m==j) and not(g+n==a and h+m==b) and not(g+n==x and h+m==y) and not(g+n==o and p+m==y)):
                r6=g+n
                c6=h+m
                str1=str
                str1+=l[r6][c6]
                check(str1,i,j,a,b,x,y,o,p,g,h,r6,c6,0,0,6)
def seven(i,j,a,b,x,y,o,p,g,h,r6,c6,str,l):
    for n in range(-1,2):
        for m in range(-1,2):
            if(not(n==0 and m==0) and r6+n>-1 and r6+n<4 and c6+m>-1 and c6+m<4 and not(r6+n==i and c6+m==j) and not(r6+n==a and c6+m==b) and not(r6+n==x and c6+m==y) and not(r6+n==o and c6+m==y) and not(o+n==o and p+m==y)):
                r7=r6+n
                c7=c6+m
                str1=str
                str1+=l[r7][c7]
                check(str1,i,j,a,b,x,y,o,p,g,h,r6,c6,r7,c7,7)
                
                
f=open("cor.txt","w")
f.write("{")
a=input()
i=0
j=0
k=0
bp=1
count=0
l=[[],[],[],[]]
while i<len(a):
    if a[i] == '2':
        p=a[i+1]+a[i+2]
        i+=3
    elif a[i]=='3':
        p=a[i+1]+a[i+2]+a[i+3]
        i+=4
    else:
        p=a[i]
        i+=1
    l[j].append(p)
    k+=1
    if k==4:
        j+=1
        k=0
    p=""
print(l)    
for i in range(0,4):
    for j in range(0,4):
        two(i,j,l)
f.write("}")    
f.close()
