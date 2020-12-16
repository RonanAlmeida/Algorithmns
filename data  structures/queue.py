"""
queue first in first out

0 0 0 0 0
left is front 
right is back

- enqueue() add to the end
- dequeue() remove from front
"""

class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        self.items.remove()
    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items)==0

    def __str__(self):
        return str(self.items)
    

if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(44)
    q.enqueue(5553)
    q.dequeue()
    print(q)