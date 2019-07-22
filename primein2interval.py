m,n=map(int,input().split())
for a in range(m+1,n):
  for b in range(2,a):
    if(a%b==0):
      break
  else:
    print(a,end=" ")
