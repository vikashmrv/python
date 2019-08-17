l=[]
n=int(input())
l=list(map(int,input().strip().split()))[:n]
v=sorted(l)
for i in v:
  print(i,end=" ")
