# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Helper recursive function, given a list of ordered numbers, it returns a list with all possible BTS
    def allTrees(self, nums):
        #Base case
        if not nums:
            return [None]
        
        answer = []
        n = len(nums)
        
        #Construct tree with roots taking all posible values
        for i in range(n):
            childs = [(l,r) for l in self.allTrees(nums[:i]) for r in self.allTrees(nums[i+1:])]
            for left_child, right_child in childs:
                Node = TreeNode(val=nums[i], left=left_child, right=right_child)
                answer.append(Node)
                
        return answer
        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = [i+1 for i in range(n)]
        return self.allTrees(nums)
        
        
        
        
        
        