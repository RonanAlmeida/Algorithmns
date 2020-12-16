"""
Stacks in python

Functions:

 -push
 -pop
 -peek
 -is_empty
 -size

"""

class Stack:

    def __init__(self):
        self.items=[] # items for the object


    def is_empty(self):
        return self.size()==0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    

if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.pop()
    s.push(3)
    s.push(4)
    s.push(44)
    s.push(232)
    s.pop()
    print(s)
    print(s.is_empty())
    print(s.peek())
    