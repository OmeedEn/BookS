import numpy as np
import ArrayStack
#import BinaryTree
#import ChainedHashTable
#import DLList
#import operator

class Calculator:
    stack = ArrayStack.ArrayStack()

    def __init__(self) :
        self.dict = None #ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)
        
    def matched_expression(self, s : str) -> bool :
        # todo
        stack = ArrayStack.ArrayStack()
        #if stack.n == 0:
            #raise IndexError()
        for char in s:
            try:
                if char == '(':
                    stack.push(char)
                if char == ')':
                    stack.pop()

            except Exception as e:
                return False

        if stack.size() == 0:
            return True

        return False






    def build_parse_tree(self, exp: str) ->str:
        # todo
        pass 

    def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        # todo
        pass 

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
        
        
