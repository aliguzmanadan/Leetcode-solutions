# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #Base case
        if len(inorder) == 0:
            return None
        
        #Find value of the root
        root_val = postorder[-1]
        node = TreeNode(val= root_val)
        
        #Left and right subtrees
        ind = inorder.index(root_val)
        left_inorder = inorder[: ind]
        left_postorder = postorder[: ind]
        right_inorder = inorder[ind+1 :]
        right_postorder = postorder[ind : -1]
        
        #Call the function recursively for the left and right childs of node
        node.left = self.buildTree(left_inorder, left_postorder)
        node.right = self.buildTree(right_inorder, right_postorder)
        return node
    
    