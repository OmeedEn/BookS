from SLLQueue import SLLQueue
from DLLDeque import DLLDeque
from DLList import DLList


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        DLList.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x : object):

        SLLQueue.add(self, x)
        if (self.max_deque.size() == 0):  # Check that there is an element in the list
            self.max_deque.add_first(x)  # If there is no element x is max
        else:
            if x > self.max_deque.get(0):  # Checks to see if x is greater than the first element in max_deque
                self.max_deque = DLLDeque()  # Re-initializes the list
                self.max_deque.add_first(x)  # Adds x to the list at the front
            else:  # x is not greater than the first element
                tail = self.max_deque.get(self.max_deque.size() - 1)  # Gets the position of the tail in the list
                while (x > tail):  # While loop for if the x is greater than the tail
                    self.max_deque.remove_last()  # Removes the element at the tail
                    tail = self.max_deque.get(self.max_deque.size() - 1)  # Gets the new position of the tail
                self.max_deque.add_last(x)  # Adds the x element to the tail of the list
                '''
                SLLQueue.add(self, x)
        if self.max_deque.size() == 0:
            self.max_deque.add(0, x)
        else:
            while self.max_deque.size() != 0 and x > self.max_deque.dummy.prev.x:
                self.max_deque.remove(self.max_deque.n-1)
            self.max_deque.add(self.max_deque.n, x)
                '''



    def remove(self) -> object:
        if self.n == 0:
            raise IndexError
        r = SLLQueue.remove(self)
        if self.max_deque.size() > 0:
            if r == self.max():
                self.max_deque.remove(0)
        return r


    def max(self):
        '''
        	returns the maximum element stored in the queue
        '''
        return self.max_deque.get(0)


'''
    #adds an element to the end of this max queue
	#INPUT: x the element to add

    SLLQueue(self, x)
     if max_queue is empty
        add x to front
    else 
        determine the max 
        how many items are in max_deque 
        if x > max
            create and reassing new list
            add x
        else
            get tail 
            while x > tail 
                remove tail
                get next tail for comparison
            add x last
        '''
'''
	removes and returns the element at the head of the max queue

    r = SSLQueue.remove(self. x)
    if we have items in max_deque
        check if r was equal to max
            remove the head of max_deque
    return r 
        '''

# TESTER
"""
def main():
    mq = MaxQueue()
    mq.add(3)
    print("Added:", 3)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    print("Max element", mq.max(), "\n\n")

    mq.add(2)
    print("Added:", 2)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    print("Max element", mq.max(), "\n\n")

    mq.add(1)
    print("Added:", 1)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    print("Max element", mq.max(), "\n\n")

    mq.add(4)
    print("Added:", 4)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")
        
"""

if __name__ == '__main__':
        main()