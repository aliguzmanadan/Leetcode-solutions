class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_left = nums[0]
        min_right = nums[-1]
        n = len(nums)
        smallest_index = -1
        biggest_index = -2
        
        for i in range(n):
            if nums[i] >= max_left:
                max_left = nums[i]
            else:
                biggest_index = i
                
            if nums[n-1-i] <= min_right:
                min_right = nums[n-1-i]
            else:
                smallest_index = n-1-i
                
        return biggest_index - smallest_index + 1
                
        