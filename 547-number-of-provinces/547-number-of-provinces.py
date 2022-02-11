#We implemnent a DisjointSet class optimized with Union by Rank and path Compression 
class DisjointSetOpt:

    #Construct the structure of a given size
    #Initially all ranks are 1 since all nodes are their own roots
    #Initially there all nodes are isolated
    def __init__(self, size):
        self.array = [x for x in range(size)]
        self.rank = [1] * size
        self.number_islands = size 

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
        #Decrease the amount of islands by one since we are connecting two different islands
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.array[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]: 
                self.array[rootX] = rootY
            else:
                self.array[rootX] = rootY
                self.rank[rootY] += 1
                
            self.number_islands -= 1
    
    #Return amount of isolated graphs
    def numberIsolated(self):
        return self.number_islands




class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = DisjointSetOpt(n)
        
        for i in range(n-1):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph.union(i,j)
                    
        return graph.numberIsolated()
                    
        