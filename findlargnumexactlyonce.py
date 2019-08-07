a=int(input())
b=(int(i) for i in input().split())
g=sorted(b,reverse=True)
i=0
while i<a:
  print(g[i],end="")
  i+=1
