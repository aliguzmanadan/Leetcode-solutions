class Solution:
    def adjacencyList(self, n, edges):
            adjancencyList = [[] for i in range(n)]
            for a, b in edges:
                adjancencyList[a].append(b)
                adjancencyList[b].append(a)

            return adjancencyList

    def validPathRecursive(self, adjList, source, destination, visited=set()):
        visited.add(source)
        if source == destination:
            return True

        for neighbor in adjList[source]:
            if neighbor not in visited and self.validPathRecursive(adjList, neighbor, destination, visited):
                return True

        return False

    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = self.adjacencyList(n, edges)
        return self.validPathRecursive(adjList, source, destination, visited = set())
        
        
        