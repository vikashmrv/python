n=int(input())
m=list(map(int,str(n)))
v=list(map(lambda x:x**3,m))
if(sum(v)==n):
  print("yes")
else:
  print("no")
