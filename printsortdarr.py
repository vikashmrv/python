l=[]
n=int(input())
l=list(map(int,input().strip().split()))[:n]
m=sorted(l)
for i in m:
  print(i,end=" ")
