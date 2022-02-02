# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root == None:
            return answer
        
        stack = [root]
        
        #Fill answer with postorder elements reversed
        while len(stack) > 0:
            node = stack.pop()
            answer.append(node.val)
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
                
        #getting answer with the correct order
        answer.reverse()
        return answer
            
        
            
                    