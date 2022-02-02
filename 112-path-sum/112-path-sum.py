# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.answer = False
        
    def hasPathSumRecursive(self, root, sum_, target):
        sum_ += root.val
        if root.left == None and root.right == None:
            if sum_ == target:
                self.answer = True
                return
        if root.left:
             self.hasPathSumRecursive(root.left, sum_, target)
        if root.right:
             self.hasPathSumRecursive(root.right, sum_, target)   
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        self.hasPathSumRecursive(root, 0, targetSum)
        return self.answer
        
        
        