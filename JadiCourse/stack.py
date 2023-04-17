from typing import Any


class MinMaxStack:
    def __init__(self, max_size):
        self.max_size=max_size
        self.top=-1
        self.items=[]
        self.nums=0
        self.get_min = None
    def push(self, value: Any) -> None:  # Time Complexity: O(1)
        self.top+=1
        self.nums+=1
        self.items.append(value)

    def pop(self) -> Any:  # Time Complexity: O(1)
        self.items.pop(self.top)
        self.top-=1
        self.nums-=1


    def size(self) -> int:
        return self.nums

    def top(self) -> bool:  # Time Complexity: O(1)
        return self.items[self.nums]
    def is_empty(self) -> bool:  # Time Complexity: O(1)
        return self.nums==0

    def is_full(self) -> bool:  # Time Complexity: O(1)
        return self.top==self.nums

    def get_min(self) -> Any:  # Time Complexity: O(1)
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}".format(self.get_min))
    def get_max(self) -> Any:  # Time Complexity: 
        if self.top is None:
            return "Stack is empty"
        else:
            print("Maximum Element in the stack is: {}" .format(self.get_max))
        


    # Driver program to test above class
# stack = Stack()
#
# stack.push(3)
# stack.push(5)
# stack.getMin()
# stack.push(2)
# stack.push(1)
# stack.getMin()
# stack.pop()
# stack.getMin()
# stack.pop()
# stack.peek()

# This code is contributed by Blinkii
