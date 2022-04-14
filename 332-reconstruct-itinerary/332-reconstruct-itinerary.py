from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        #Create graph of airport with adjancency list
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src] += [dst]

        #Order children lists in descending order, so we pop lexicographically smaller elements first
        for src in graph:
            graph[src].sort(reverse=True)
            
        stack, it = ["JFK"], []
            
        #Traverse the Graph using DSF, we go as deep as possible unitl we reach an airport 
        #that cannot be departed from. That is our last destination
        while stack:
            curr = stack[-1]
            
            if curr in graph and graph[curr]:
                stack.append(graph[curr].pop())
            else:
                it.append(stack.pop())
                
        return it[::-1]
        
        