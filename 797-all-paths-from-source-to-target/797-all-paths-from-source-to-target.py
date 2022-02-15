class Solution:
    
    #Recursive function that, given a start A and destination B,
    #returns the list of all paths from A to B
    def allPathsSourceTargeRecursive(self, graph, start, destination):
        
        #Base case: If start == destination then there is only one path 
        if start == destination:
            return[[start]]
        
        #Otherwise look for paths starting in the neighborhs of start
        paths = []
        for neighbor in graph[start]:
            paths += [[start] + p for p in self.allPathsSourceTargeRecursive(graph, neighbor, destination)]
        
        return paths
            
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.allPathsSourceTargeRecursive(graph, 0, len(graph)-1)
        