x,y=map(int,input().split())
l=list(map(int,input().split()))
c=[]
for i in range(0,y):
    d = []
    d=list(map(int,input().split()))
    s = l[d[0]-1]
    for j in range(min(d),max(d)):
        s=s^l[j]
    c.append(s)
for i in range(0,len(c)):
    print(c[i]) 
