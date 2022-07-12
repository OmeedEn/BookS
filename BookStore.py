import Book
import ArrayList
import ArrayQueue
import MaxQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
import AdjacencyList
import time
import copy
import algorithms


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    '''
    def __init__(self) :
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()


    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key,
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.bookIndices.add(key, self.bookCatalog.size() - 1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size()-1)

            # The following line is used to calculate the total time
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")


    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, key):
      #dtermine if key is inside the Chainedhashtable
      # if inside Chainedhashtable then get the varibale
      # get the book for adding shopping cart
      # put book inside the shopping cart
      # print the title
      # if not inside print did not find
        if self.bookIndices.find(key) != None:
            book = self.bookIndices.find(key)
            o = self.bookCatalog.get(book)
            self.shoppingCart.add(o)
            print(f"Added Title: {o.title} ")
        else:
            print("Book not found")

    def addBookByPrefix(self, prefix: str):
        if prefix == "":
            print("Book not found ")
            return False
        else:
            index = self.sortedTitleIndices.find(prefix)
            val = index.v
            if val is not None:
                self.addBookByIndex(val)
                return True
        return False


    def searchBookByInfix(self, infix : str) :
        '''
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        '''
        start_time = time.time()
        # todo
        # if infix in title:
        # special case where we only print 50 books
        # ""
        s = 0
        cur = self.bookCatalog.dummy.next
        while cur != self.bookCatalog.dummy:
            book = cur.x
            if infix in book.title:
                print(book)
                s += 1
            if s == 50:
                break
            cur = cur.next
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.max()
            print(f"Best seller is: {u}")


    def bestsellers_with(self, infix, structure, n = 0):

        bst = BinarySearchTree.BinarySearchTree()
        bh = BinaryHeap.BinaryHeap()
        if n == "":
            n = 0
        else:
            n = int(n)
        if infix == "":
            print("invalid infix")
        else:
            start_time = time.time()
            if structure != "1" and structure != "2":
                print("Invalid data structure")
            else:
                if n < 0:
                    print("Invalid number of titles")

                elif structure == "1":
                    if n == 0:
                        for book in self.bookCatalog:
                            if infix in book.title:
                                bst.add(book.rank, book)
                    else:
                        for book in self.bookCatalog:
                            if infix in book.title:
                                bst.add(book.rank, book)
                                n -= 1
                                if n == 0:
                                    break
                    L = bst.in_order()
                    L.reverse()
                    for i in L:
                        print(i.v)

                else:
                    if n == 0:
                        for book in self.bookCatalog:
                            if infix in book.title:
                                book.rank *= -1
                                bh.add(book)
                    else:
                        for book in self.bookCatalog:
                            if infix in book.title:
                                book.rank *= -1
                                bh.add(book)
                                n -= 1
                                if n == 0:
                                    break
                    for i in range(bh.size()):
                        x = bh.remove()
                        x.rank *= -1
                        print(x)

                elapsed_time = time.time() - start_time
                print(f"bestsellers_with({infix}, {structure}, {n}) completed in {elapsed_time} seconds")

    def sort_catalog(self, s):
        start_time = time.time()
        if s == 1:
            algorithms.merge_sort(self.bookCatalog)
        elif s == 2:
            algorithms.quick_sort(self.bookCatalog, False)
        elif s == 3:
            algorithms.quick_sort(self.bookCatalog, True)
        else:
            print("Invalid algorithm")
        elapsed_time = time.time() - start_time
        print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds")


    def search_by_prefix(self, prefix, algo):
        # deepcopy of catalog
        # determine which algorithm
        # if LS don't need to sort, we do in if in BS
        # loop through WHOLE catalog
        #   find by title using LS
        #   if we don't find anything break
        #   if we do, get the index from LS
        #   print the book
        #   increment the count
        #   remove book from copy catalog

        copyc = ArrayList.ArrayList()
        for i in range(self.bookCatalog.size()):
            copyc.append(self.bookCatalog.get(i))
        count = 0
        start_time = time.time()

        if algo == 1:
            pre_book = Book.Book("blank", prefix, "blank", 0, "blank")
            x = algorithms.linear_search(copyc, pre_book)
            while x != -100:
                algorithms.linear_search(self.bookCatalog, prefix)
                x = algorithms.linear_search(copyc, pre_book)
                found = copyc.get(x)
                if prefix.lower() in found.title[:len(prefix)].lower():
                    print(found)
                    count += 1
                    copyc.remove(x)
                else:
                    break

        elif algo == 2:
            algorithms.quick_sort(copyc)
            pre_book = Book.Book("blank", prefix, "blank", 0, "blank")
            x = algorithms.binary_search(copyc, pre_book)
            while x != -100:
                algorithms.binary_search(copyc, prefix)
                i = algorithms.binary_search(copyc, pre_book)
                found = copyc.get(i)
                if prefix.lower() in found.title[:len(prefix)].lower():
                    print(found)
                    count += 1
                    copyc.remove(i)
                else:
                    break
        else:
            print("Invalid algorithm")

        elapsed_time = time.time() - start_time
        print(f"Found {count} books with prefix {prefix} in {elapsed_time} seconds")


    def display_catalog(self, n):
        # verify n is not greater than the size of catalog
        if n <= self.bookCatalog.size():
            for i in range(n):
                print(self.bookCatalog.get(i))



