from collections import deque

class Solution:
    #Create adjancecy list with the list of all edges
    def adjacencyList(self, n, edges):
            adjancencyList = [[] for i in range(n)]
            for a, b in edges:
                adjancencyList[a].append(b)
                adjancencyList[b].append(a)

            return adjancencyList
    
    #BSF Iterative Approach
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int, ) -> bool:
        
        ajdList = self.adjacencyList(n, edges)
        
        visited = set()
        queue = deque([[source]])

        while queue:
            #Pop first partial path available and check if it is completed
            path = queue.popleft()
            if path[-1] == destination:
                return True
            #if not the go to the next levels
            else:
                for neighbor in ajdList[path[-1]]:
                    if neighbor not in visited:
                        queue.append(path+[neighbor])
                visited.add(path[-1])

                    
<<<<<<< HEAD
        return False
            
        
        
=======
        return False
>>>>>>> 6828ef8e74c2acbe21575f60f182679d776e8619
