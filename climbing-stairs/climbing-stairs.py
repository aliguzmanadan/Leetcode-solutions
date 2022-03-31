class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0,1]
        for i in range(n):
            temp = f[0]+f[1]
            f[0] = f[1]
            f[1] = temp
        return f[1]
        