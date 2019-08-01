f,g=map(int,input().split())
z=(input().split())[0:f] 
i=0
while i<g:
  m,n=map(int,input().split())
  i+=1
  print(min(z[m-1:n]))  
