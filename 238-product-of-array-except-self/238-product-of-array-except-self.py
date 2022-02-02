class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [1]
        R = [1]
        n = len(nums)
        answer = []
        
        for i in range(1,n):
            L.append(L[-1]*nums[i-1])
            R.append(R[-1]*nums[n-i])
            
        for i in range(n):
            answer.append(L[i]*R[n-1-i])
            
        return answer