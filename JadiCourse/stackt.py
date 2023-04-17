class Stack:
    def __init__(self):
        self.elements =[]
    def push(self,data):
        self.elements.append(data)
    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            return None
    def size(self):
        return len(self.elements)
    def empty(self):
        return True if self.size() == 0 else False
    def peek(self):
        return self.elements[-1]


stack = Stack()
stack.push("Ailin")
stack.push('Mahdi')
print(stack.__dict__)
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())
print("Number of elements in stack is :{}".format(stack.size()))
print(stack.empty())
print(stack.peek())