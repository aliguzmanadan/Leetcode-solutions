# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #initialize Max variable to store the maximum seen at a certain moment in the inroder traversal
        Max = float(-inf)
        
        #iterative inorder traversal
        stack = []
        current = root
        
        while (len(stack) > 0) or (current != None):
            while current != None:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            
            #Check if the inroder traversal is indeed increasing and update Max
            if current.val <= Max:
                return False
            Max = current.val
            current = current.right
            
        #If inorder traversal is fully completed return true
        return True
       