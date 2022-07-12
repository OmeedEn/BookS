from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0
        
    def clear(self):
        self.r = None
        self.n = 0

    def new_node(self, x, v=None):
        u = BinaryTree.Node(x, v)
        u.left = u.right = u.parent = None
        return u

    def find_eq(self, x : object) -> object:
        # todo

        h = self.r
        while h is not None:
            if x < h.x:
                h = h.left
            elif x > h.x:
                h = h.right
            else:
                return h
        return h

    def find_last(self, x : object) -> BinaryTree.Node:
        # todo

        w = self.r
        prev = None
        while w is not None:
            if x < w.x:
                prev = w
                w = w.left
            elif x > w.x:
                prev = w
                w = w.right
            else:
                return w
        return prev

    def find(self, x: object) -> object:
        # todo

        w = self.r
        z = None
        while w is not None:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return z

    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        # todo
        if p is None:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True


        
    def add_node(self, u : BinaryTree.Node) -> bool:

        p = self.find_last(u.x)
        return self.add_child(p, u)




    def add(self, key : object, value : object) -> bool:
        # todo

        return self.add_child(self.find_last(key), self.new_node(key, value))
        # self.new_node(key, value)

    def get(self, key : object) -> object:
        # todo

        w = self.r
        while w is not None:
            if key < w.x:
                w = w.left
            elif key > w.x:
                w = w.right
            else:
                return w.v
        return None


    def splice(self, u: BinaryTree.Node):
        # todo
        if u.left is not None:
            s = u.left
        else:
            s = u.right
        p = None
        if u == self.r:
            self.r = s
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != None:
            s.parent = p
        self.n -= 1

    def remove_node(self, u : BinaryTree.Node):
        # todo
        if u is not None or u.left is None:
            if u.left is None or u.right is None:
                self.splice(u)
            else:
                w = u.right
                while w.left is not None:
                    w = w.left
                u.x = w.x
                u.v = w.v
                self.splice(w)
            return u.v
        return None


    def remove(self, x : object) -> bool:
        # todo
        if self.find(x) is None:
            raise ValueError
        return self.remove_node(self.find(x))

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.x
            u = self.next_node(u)

