class Solution:
    #Create adjancecu list with the list of all edges
    def adjacencyList(self, n, edges):
            adjancencyList = [[] for i in range(n)]
            for a, b in edges:
                adjancencyList[a].append(b)
                adjancencyList[b].append(a)

            return adjancencyList

    def validPathRecursive(self, adjList, source, destination, visited=set()):
        visited.add(source)

        #Base case
        if source == destination:
            return True

        #There is a path from A to B, if there is path from a neighbor of A to B
        for neighbor in adjList[source]:
            if neighbor not in visited and self.validPathRecursive(adjList, neighbor, destination, visited):
                return True

        #If no neighbor of A has a path to B, there there is no path from A to B
        return False

    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = self.adjacencyList(n, edges)
        return self.validPathRecursive(adjList, source, destination, visited = set())