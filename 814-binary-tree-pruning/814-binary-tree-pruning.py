# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Base case
        if root == None:
            return None
        
        #Prune left and right subtrees
        root.right = self.pruneTree(root.right)
        root.left = self.pruneTree(root.left)
        
        #Prune current tree is possible
        if (not root.right) and (not root.left) and (not bool(root.val)):
            return None
        
        return root
        