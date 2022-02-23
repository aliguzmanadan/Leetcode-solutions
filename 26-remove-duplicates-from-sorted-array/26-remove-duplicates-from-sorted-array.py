class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Initialize two pointers in the array, and k (number of different elementes)
        i, j = 0, 0
        k = 1
        
        #Search with the pointer j until a[j]!=a[i], then change i <- i+1  and make a[i] = a[j], 
        #Repeat this until j reaches the end of the array
        while j < len(nums):
            
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            i += 1

            if j <= len(nums)-1:
                nums[i] = nums[j]
                k += 1
        return k
            
        