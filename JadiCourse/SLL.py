class Node :
    def __init__(self, val):
        self.value = val
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        
    def add(self, val):
        if self.empty() is True:
            self.head = Node(val)
            print("Head value created.")
            return
        
        option = int(input("Enter 1 to add a Node at the beginning\nEnter 2 to add a Node at the end\nEnter 3 to add a Node in the middle: "))
        if option == 1:
            a = Node(val)
            a.next = self.head
            self.head = a
            
        elif option == 2:
            i = self.head
            
            while i.next is not None:
                i = i.next
            i.next = Node(val)
            
        elif option == 3:
            pos = int(input("Enter the position: "))
            i = 1
            n = self.head
            f = n.next
            flag = 0
            
            while f is not None:
                if i == pos:
                    flag = 1
                    break
                f = f.next
                n = n.next
                i = i + 1
            if flag == 1:
                n.next = Node(val)
                n.next.next = f
            else:
                print("Position not found.")
                
    def delete(self):
        if self.empty() is True:
            print("Linked List empty.")
            return
        
        elif self.head.next is None:
            self.head = None
            return
        
        option = int(input("Enter 1 to delete the beginning element\nEnter 2 to delete the last element\nEnter 3 to delete elements in between: "))
        if option == 1:
            self.head = self.head.next

        elif option == 2:
            n = self.head
            
            while n.next.next is not None:
                n = n.next
            n.next = None

        else:
            option = int(input("Enter 1 to delete by position\nEnter 2 to delete by value: "))
            
            if option == 1:
                pos = int(input("Enter the position: "))
                i = 1
                n = self.head
                f = self.head.next
                flag = 0
                
                while f.next is not None:
                    if i == pos:
                        flag = 1
                        break
                    i = i + 1
                    n = n.next
                    f = f.next
                    
                if flag == 1:
                    n.next = f.next
                    
                else:
                    print("Position not found.")
                    return
                
            else:
                val = int(input("Enter the value you want to delete: "))
                n = self.head
                f = self.head.next
                flag = 0
                while f.next is not None:
                    if f.value == val:
                        flag = 1
                        break
                    f = f.next
                    n = n.next
                if flag == 1:
                    n.next = f.next
                else:
                    print("Value not found.")
                    return
                
    def clear(self):
        self.head = None
        print("Linked List cleared.")
        
    def empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def display(self):
        if self.empty() is True:
            print("Linked List empty.")
            return
        print("THE LINKED LIST HEAD ===> ", self.head.value)
        n = self.head.next
        while n is not None:
            print(n.value)
            n = n.next
        print("Linked List ends")
        
LL = SLL()
while True:
    option = int(input("Enter 1 to add an element\nEnter 2 to delete an element\nEnter 3 to clear the Linked List\nEnter 4 to display the Linked List\nEnter 5 to exit: "))
    if option == 1:
        value = int(input("Enter the value you want to add: "))
        LL.add(value)
        continue
    elif option == 2:
        LL.delete()
        continue
    elif option == 3:
        LL.clear()
        continue
    elif option == 4:
        LL.display()
        continue
    elif option == 5:
        print("Goodbye.")
        break
    elif option == 6:
        print(LL.empty())
    else:
        print("Wrong option.")