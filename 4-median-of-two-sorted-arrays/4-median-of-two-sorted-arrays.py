class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        
        #Ensuring that the first input has a smaller amout of elements
        if y < x:
            return self.findMedianSortedArrays(nums2, nums1)
        
        #We now perform binary search on the first input
        #First define the start and ending point of the array where 
        start=0
        end = x
        
        #Binary search loop
        while (start <= end):
            partX = (start+end)//2
            partY = (x+y+1)//2 - partX
            
            #Get max elements to the left part of the partition on nums 1 and nums2
            maxLeftX = nums1[partX-1] if (partX != 0) else float('-inf')
            maxLeftY = nums2[partY-1] if (partY != 0) else float('-inf')
            
            #Get min elements to the right part of the partition on nums 1 and nums2
            minRightX = nums1[partX] if (partX != x) else float('inf')
            minRightY = nums2[partY] if (partY != y) else float('inf')
            
            #Check wheter we have found the correct partition
            if (maxLeftX <= minRightY) and (maxLeftY <= minRightX):
                #Here we found the correct partition so we canr return the median
                if (x+y)%2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
                
            elif maxLeftX > minRightY:
                #Here we are to far to the righ of X
                end = partX - 1
                
            else:
                #Here we are to far to the left of X
                start = partX + 1
                
                
                
                
                
        