class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentMin = prices[0]
        
        for i in range(1,len(prices)):
            maxProfit = max(maxProfit, prices[i] - currentMin)
            currentMin = min(currentMin, prices[i])
            
        return maxProfit