class Solution:
    #Create adjancecy list with the list of all edges
    def adjacencyList(self, n, edges):
            adjancencyList = [[] for i in range(n)]
            for a, b in edges:
                adjancencyList[a].append(b)
                adjancencyList[b].append(a)

            return adjancencyList
    
    #Iterative Approach
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int, ) -> bool:
        
        ajdList = self.adjacencyList(n, edges)
        
        visited = set()
        stack = [source]
        
        while stack:
            #pop top element from stack and process it
            node = stack.pop()
            if node == destination:
                return True
            
            
            visited.add(node)
            
            for neighbor in ajdList[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
        return False
            