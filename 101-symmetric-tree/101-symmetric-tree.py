# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self, root1, root2):
        """Determines whether two trees are mirror to each other"""
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        elif root1.val != root2.val:
            return False
        return self.mirror(root1.left, root2.right) and self.mirror(root1.right, root2.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.mirror(root.left, root.right)
    
    