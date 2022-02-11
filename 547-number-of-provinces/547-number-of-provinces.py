#We implemnent a DisjointSet class optimized with Union by Rank and path Compression 
class DisjointSetOpt:

    #Construct the structure of a given size
    #Initially all ranks are 1 since all nodes are their own roots
    def __init__(self, size):
        self.array = [x for x in range(size)]
        self.rank = [1] * size

    #Find the root of a node x and update roots recursively
    def findRoot(self, x):
        if self.array[x] == x:
            return x
        self.array[x] = self.findRoot(self.array[x])
        return self.array[x]
    
    #Connect two nodes
    def union(self, x, y):
        rootX = self.findRoot(x)
        rootY = self.findRoot(y)

        #If the roots are different, check for the rank of the roots
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.array[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]: 
                self.array[rootX] = rootY
            else:
                self.array[rootX] = rootY
                self.rank[rootY] += 1
    
    #Return amount of isolated graphs
    def numberIsolated(self):
        roots_set = set({})
        for i in range(len(self.array)):
            root = self.findRoot(i)
            roots_set.add(root)
        return len(roots_set)




class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = DisjointSetOpt(n)
        
        for i in range(n-1):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph.union(i,j)
                    
        return graph.numberIsolated()
                    
        