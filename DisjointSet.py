class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def make_set(self, i): # O(1)
        self.parent[i] = i # every element starts by pointing to itself
        self.rank[i] = 0
    
    def find(self, i): # O(lg n)
        while self.parent[i] != i:
            i = self.parent[i]
        return i
    
    def union(self, i, j): # O(lg n)
        i = self.find(i)
        j = self.find(j)
        if i != j:
            if self.rank[i] < self.rank[j]:
                self.parent[i] = j
            elif self.rank[i] > self.rank[j]:
                self.parent[j] = i
            else:
                self.rank[i] += 1
                self.parent[j] = i