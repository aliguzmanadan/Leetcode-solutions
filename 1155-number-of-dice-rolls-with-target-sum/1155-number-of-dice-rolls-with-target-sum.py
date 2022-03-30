import math

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n*k < target:
            return 0
        
        return math.comb(n*k-target+n-1, n-1) % int(math.pow(10,9) + 7)
        
        