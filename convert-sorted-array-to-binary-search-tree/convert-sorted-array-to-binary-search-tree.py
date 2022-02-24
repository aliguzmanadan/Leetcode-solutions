# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        half_idx = math.floor(len(nums)//2)
        Node = TreeNode(nums[half_idx])
        Node.left = self.sortedArrayToBST(nums[:half_idx])
        Node.right = self.sortedArrayToBST(nums[half_idx+1:])
        return Node
    
    
        