from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #initialize paths, queue, n, (we dont need to keep track of visited vertices since its is a acyclic graph!)
        paths = []
        n = len(graph)
        queue = deque([[0]])

        while queue:

            #Pop first partial path available and check if it is completed
            path = queue.popleft()
            if path[-1] == n-1:
                paths.append(path)

            #if not the go to the next levels
            else:
                for neighbor in graph[path[-1]]:
                        queue.append(path+[neighbor])

        return paths
        