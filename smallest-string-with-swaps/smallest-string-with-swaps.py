from collections import defaultdict 

#This is my implementation of the DisjointSet Class optimized with Union by rank and Path Compression
class DisjointSetOpt:

    #Construct the structure of a given size
    #Initially all ranks are 1 since all nodes are their own roots
    #Initially there all nodes are isolated
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
        #Decrease the amount of islands by one since we are connecting two different islands
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.array[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]: 
                self.array[rootX] = rootY
            else:
                self.array[rootX] = rootY
                self.rank[rootY] += 1
                

    #Return dict of all islands (key = root, value = list of all island elements)
    def Islands(self):
        islands_dict = defaultdict(list)
        for i in range(len(self.array)):
            root = self.findRoot(i)
            islands_dict[root].append(i) 
        return islands_dict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #Convert string into list to have a mutable object to modify 
        n = len(s)
        answer = list(s)
        
        
        #Join all pairs in a Disjoint set
        graph = DisjointSetOpt(n)
        for pair in pairs:
            graph.union(pair[0], pair[1])
            
        #Get all the islands
        disjointSets = graph.Islands()
        
        #Sort substrings determined by each island separtely
        for root in disjointSets:
            #Order characters corresponding to each island lexicographycally
            chars = [s[i] for i in disjointSets[root]]
            chars.sort()
            
            #Put the ordered substrings back in s
            for i in range(len(chars)):
                answer[disjointSets[root][i]] = chars[i]
                
        return "".join(answer)
            
            
            