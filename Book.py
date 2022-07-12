class Book:
    '''
    Class: Book contains the detail of the books. It allows comparing
    two instances accoring to the rank.
    for example b1 < b2 if  b1.rank < b2.rank
    '''

    def __init__(self, key, title, group, rank, similar):
        self.key = key
        self.title = title
        self.group = group
        self.rank = int(rank)
        self.similar = similar

    def __lt__(self, a):
        '''
        This function allows to make direct comparation using the operator <
        '''
        return str(self.title).lower() < str(a.title).lower()

    def __le__(self, a):
        return str(self.title).lower() <= str(a.title).lower()

    def __gt__(self, a):
        '''
        This function allows to make direct comparation using the operator >
        '''
        return str(self.title).lower() > str(a.title).lower()

    def __ge__(self, a):
        return str(self.title).lower() >= str(a.title).lower()

    def __eq__(self, a):
        s1 = str(self.title).lower()
        s2 = str(a.title).lower()
        m = min(len(s1), len(s2))
        if s1[:m] == s2[:m]:
            return True
        else:
            return False


    def __str__(self):
        '''
        function returns a string containting the book information
        '''
        return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}"


