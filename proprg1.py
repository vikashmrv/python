v=int(input())
m=[]
for i in range(0,v):
  log=input()
  m.append(log)
v=[]
for i in zip(*m):
  if(i.count(i[0])==len(i)):
    v.append(i[0])
  else:
    break
print(''.join(v))
