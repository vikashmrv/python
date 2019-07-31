rev= ' '
num= input()
for i in range(len(num), 0, -1):
    rev += num[i-1]
print(int(rev))
