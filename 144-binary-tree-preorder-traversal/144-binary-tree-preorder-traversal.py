# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root == None:
            return answer
        
        nStack = [root]
        
        while len(nStack) > 0:
            node = nStack.pop()
            answer.append(node.val)
            
            if node.right:
                nStack.append(node.right)
                
            if node.left:
                nStack.append(node.left)
                
        return answer
        
        
        
        