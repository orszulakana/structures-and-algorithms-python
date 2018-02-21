from data_structures.Stack import *

Stack = Stack()

for i in range(0, 10):
    Stack.Push(i)

length = Stack.Size()
print('Stack size: ', length)

print('Elements on stack :')
for i in range(length):
    print(Stack.Top())
    Stack.Pop()
