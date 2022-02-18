"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #No nodes case
        if node == None:
            return None
        
        visited = set()
        new_nodes = {}
        stack = [node]
        
        while stack:
            curr = stack.pop()
            
            for neighbor in curr.neighbors:
                #Create copy of neighbor in dict if not there yet
                if neighbor.val not in new_nodes:
                    new_nodes[neighbor.val] = Node(neighbor.val)
                    
                #Add neighbor to stack if it hasn't been visited yet
                if neighbor.val not in visited:
                    stack.append(neighbor)
                    
            #create copy of current node if thre isn't one yet
            if curr.val not in new_nodes:
                new_nodes[curr.val] = Node(curr.val)
                
            #Make the copy complete and mark current node as visited
            new_nodes[curr.val].neighbors = [new_nodes[n.val] for n in curr.neighbors]
            visited.add(curr.val)
            
        return new_nodes[1]
            
                    
                    
        
                    
                    
                    
                    
                    
                    
        