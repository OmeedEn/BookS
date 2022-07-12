"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        # todo
        #check for duplicates
        if not self.adj[i].contains(j):
            self.adj[i].append(j)


    def remove_edge(self, i : int, j : int):
        # todo
        for k in range(0, len(self.adj[i])):
            if self.adj[i][k] == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        for k in range(len(self.adj[i])):
            if self.adj[i][k] == j:
                return True
        return False

    def out_edges(self, i) -> List:
        # todo
        return self.adj[i]

    def in_edges(self, j) -> List:
        # todo
        in_ed = ArrayList.ArrayList()
        for i in range(self.n - 1):
            if self.has_edge(i, j):
                in_ed.append(i)
        return in_ed

    def bfs(self, r : int):
        # todo
        traversal = ArrayList.ArrayList()
        seen = np.array([0, 0, 0, 0, 0, 0, 0], dtype=bool)
        q = ArrayQueue.ArrayQueue()
        traversal.append(r)
        seen[r] = True
        q.add(r)
        while q.size() > 0:
            cur = q.remove()
            neighbors = self.out_edges(cur)
            for i in range(0, len(neighbors)):
                neighbor = neighbors[i]
                if not seen[neighbor]:
                    traversal.append(neighbor)
                    seen[neighbor] = True
                    q.add(neighbor)
        return traversal

    def dfs(self, r : int):
        # todo
        traversal = ArrayList.ArrayList()
        seen = ArrayList.ArrayList()
        q = ArrayStack.ArrayStack()
        for i in range(self.n):
            seen.append(False)
        q.push(r)
        while q.size() > 0:
            cur = q.pop()
            neighbors = self.out_edges(cur)
            # for i in range(0, len(neighbors)):
            #     neighbor = neighbors[i]
            if seen[cur] == False:
                seen[cur] = True
                traversal.append(cur)
                for i in range(len(neighbors)-1, -1, -1):
                    q.push(neighbors[i])
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s



def main():
    g = AdjacencyList(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(1, 4)
    g.add_edge(4, 5)

    print(g)
    print("BFS(0)", g.bfs(0))

# g = AdjacencyList(12)
# g.add_edge(0, 1)
# g.add_edge(0, 9)
# g.add_edge(1, 0)
# g.add_edge(1, 2)
# g.add_edge(1, 10)
# g.add_edge(1, 11)
# g.add_edge(2, 1)
# g.add_edge(2, 3)
# g.add_edge(2, 11)
# g.add_edge(3, 2)
# g.add_edge(3, 4)
# g.add_edge(4, 3)
# g.add_edge(4, 5)
# g.add_edge(4, 11)
# g.add_edge(5, 4)
# g.add_edge(5, 6)
# g.add_edge(6, 5)
# g.add_edge(6, 7)
# g.add_edge(6, 11)
# g.add_edge(7, 6)
# g.add_edge(7, 8)
# g.add_edge(7, 10)
# g.add_edge(8, 7)
# g.add_edge(8, 9)
# g.add_edge(9, 0)
# g.add_edge(9, 8)
# g.add_edge(9, 10)
# g.add_edge(10, 1)
# g.add_edge(10, 7)
# g.add_edge(10, 9)
# g.add_edge(10, 11)
# g.add_edge(11, 2)
# g.add_edge(11, 4)
# g.add_edge(11, 6)
# g.add_edge(11, 10)
#
# print(g)
# print("BFS(0):", g.bfs(0))
# print("Expected: [0, 1, 9, 2, 10, 11, 8, 3, 7, 4, 6, 5]")
# print("\nDFS(0):", g.dfs(0))
# print("Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]")

if __name__ == '__main__':
    main()
