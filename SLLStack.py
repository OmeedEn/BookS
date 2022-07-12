from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
   
    def push(self, x : np.object) :
       # todo

       new_node = self.Node(x)
       new_node.next = self.head
       self.head = new_node
       self.n = self.n + 1
       if self.n == 1:
           self.tail = new_node
        
    def pop(self) -> np.object:
        # todo
        if self.n == 0:
            raise IndexError
        temp = self.head.x
        self.head = self.head.next
        self.n = self.n-1
        if self.n == 0:
            self.tail = None
        return temp




    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
def main():
    stack = SLLStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)

if __name__ == '__main__':
    main()


