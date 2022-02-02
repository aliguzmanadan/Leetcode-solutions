# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
        

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root == None:
            return answer
        
        stack = []
        current = root
        
        while (len(stack) > 0) or (current != None):
            while current != None:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            answer.append(current.val)
            current = current.right
            
        return answer
    
    