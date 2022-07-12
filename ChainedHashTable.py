from Interfaces import Set
from DLList import DLList
import numpy as np

class ChainedHashTable(Set):
    class Node() :
        def __init__(self, key, value) :
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList) :
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=DLList)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key : int) -> int :
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d) 

    def size(self) -> int:
        return self.n
        
    def add(self, key : object, value : object) :
        # todo
        #append(new_node)
        new_node = self.Node(key, value)
        if self.find(key) != None:
            return False
        hash_value = self._hash(key)
        if len(self.t) == self.n:
            self.resize()
        self.t[hash_value].append(new_node)
        self.n += 1
        return True

    def find(self, key : object) -> object :
        # todo
        if self.n < 0:
            print("failed")
            return None
        for i in range(0, self.t[self._hash(key)].size(), 1):
            if self.t[self._hash(key)].get(i).key == key:
                return self.t[self._hash(key)].get(i).value
        return None

    def remove(self, key : int)  -> object:
        # todo
        if self.find(key) == None:
            print("failed")
            return None
        else:
            hash_value = self._hash(key)
            l = self.t[hash_value]
            temp = None
            for i in range(0, l.size(), 1):
                if l[i].key == key:
                    self.n -= 1
                    temp = l.remove(i)
            if len(self.t) > 3*self.n:
                self.resize()
            return temp
    
    def resize(self):
        # todo
        #self.t[h].size()
        if self.n == len(self.t):
            self.d += 1
        if len(self.t) >= 3*self.n:
            self.d -= 1
        temp = self.alloc_table(2**self.d)
        for i in range(0, len(self.t), 1):
            for j in range(0, self.t[i].size(), 1):
                current_ele = self.t[i].get(j)
                h = self._hash(current_ele.key)
                temp[h].append(current_ele)

        self.t = temp


    def __str__(self):
        s = "\n"
        for i in range(len(self.t)):
            s += str(i) + " : "
            for j in range(self.t[i].size()):
                k = self.t[i].get(j)
                s += "(" + str(k.key) + ", " + str(k.value) + "); "
            s += "\n"
        return s

def main():
    chain = ChainedHashTable()
    chain.remove(1)
    chain.add(1, "first")
    chain.find(1)
    chain.add(2, "second")
    #chain.add(3, "third")

if __name__ == '__main__':
    main()



