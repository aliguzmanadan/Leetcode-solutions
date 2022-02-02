# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def __init__(self):
        self.answer = 0
    
    def maxDephtTopButtom (self, root, depth):
        if root.left == None and root.right == None:
            self.answer = max(self.answer, depth)
        if root.left:
            self.maxDephtTopButtom(root.left, depth+1)
        if root.right:
            self.maxDephtTopButtom(root.right, depth+1)
        
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.maxDephtTopButtom (root, 1)
        return self.answer
        
        