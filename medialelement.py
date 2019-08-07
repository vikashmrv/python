v=[]
n=int(input())
l=list(map(int,input().strip().split()))[:n]
k=sorted(l)
le=len(k)
c=le//2
print(k[c])
