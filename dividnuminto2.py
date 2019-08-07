v=int(input())
n=(input().split())[0:v]
a=v//2
if v>3:
  if(a%2==0):
    print("yes")
  else:
    print("no")
else:
  if(v==3):
    print("yes")
  else:
    print("no")
