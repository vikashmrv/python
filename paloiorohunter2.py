class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
v = Stack()
text = input()
 
for character in text:
    v.push(character)
 
reversed_text = ''
while not v.is_empty():
    reversed_text = reversed_text + v.pop()
 
if text == reversed_text:
    print('YES')
else:
    print('NO')
