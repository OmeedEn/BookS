from Interfaces import List
import numpy as np
import math


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int,) -> Node:
        # todo
        if i < 0 or i > self.n:
            raise IndexError
        if i < self.n / 2:
            p = self.dummy.next
            for i in range(0, i, 1):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n - i):
                p = p.prev
        return p
        
    def get(self, i) -> np.object:
        # todo
        if i < 0 or i >= self.n:
            raise IndexError
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        # todo
        if i < 0 or i > self.n:
            raise IndexError
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y


    def reverse(self):
        # reverse the list itself
        '''
                    dummy -> next = head
                    dummy -> prev = tail
        where head is
        where tail is
        define a current pointer
        stop when we hit dummy
            temp = c.next
            c.next = c.prev
            c.prev = temp
            point current to next node
        take care of dummy
        '''
        current = self.dummy.next
        head = self.dummy.next
        tail = self.dummy.prev
        self.dummy.next = tail
        self.dummy.prev = head
        while current != self.dummy:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp


    def add_before(self, w : Node, x : np.object) -> Node:
        # todo
        new_node = DLList.Node(x)
        if w == 0:
            return Exception
        new_node.prev = w.prev
        new_node.next = w
        new_node.prev.next = new_node
        new_node.next.prev = new_node
        self.n += 1
        return new_node
            
    def add(self, i : int, x : np.object):
        # todo
        if i < 0 or i > self.n:
            return Exception
        return self.add_before(self.get_node(i), x)

    def _remove(self, w : Node) :
       # todo
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x
    
    def remove(self, i: int) :
        if i < 0 or i > self.n:
            raise IndexError
        if self.n == 0:
            raise IndexError
        return self._remove(self.get_node(i))


    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        # todo
        # [h a n n a h]
        # for(size//2)
        # use get to compare front and back
        if self.n == 0:
            return True
        front = self.dummy.next
        back = self.dummy.prev
        for q in range(0, math.floor(self.n/2), 1):
            if front.x != back.x:
                return False
            front = front.next
            back = back.prev
        return True

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

def main():
    dLL = DLList()
    dLL.isPalindrome()
    print(dLL)

    #dLL.add_before(2,3)


if __name__ == '__main__':
        main()
