from Interfaces import Queue
import numpy as np

class SLLQueue(Queue):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
        

    def add(self, x :np.object) :
        # todo
        new_node = self.Node(x)
        #new_node.x = x
        if self.n == 0:
            self.head = new_node
        elif self.n != 0:
            self.tail.next = new_node
        self.tail = new_node
        self.n += 1
        return True

    def remove(self) -> np.object:
        # todo
        if self.n == 0:
            raise IndexError
        x = self.head
        self.head = self.head.next
        self.n -= 1
        return x.x

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
    slq = SLLQueue()
    slq.add(1)
    slq.add(2)
    slq.add(3)
    slq.remove()
    slq.remove()
    print(slq)

if __name__ == '__main__':
    main()