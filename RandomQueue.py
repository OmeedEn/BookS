import numpy as np
import random 
from ArrayQueue import ArrayQueue

class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)
            

    def remove(self) -> np.object :
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # todo
        if self.n == 0:
            raise IndexError()

        r = random.randint(0, self.n - 1)
        r = (self.j + r) % len(self.a)
        temp = self.a[self.j]
        self.a[self.j] = self.a[r]
        self.a[r] = temp

        return super().remove()


        # for k in range(0, self.n):












     




