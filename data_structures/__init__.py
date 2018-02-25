from data_structures.Stack import *

Stack = Stack()

for i in range(0, 10):
    Stack.push(i)

length = Stack.size()
print('Stack size: ', length)

print('Elements on stack :')
for i in range(length):
    print(Stack.peak())
    Stack.pop()
