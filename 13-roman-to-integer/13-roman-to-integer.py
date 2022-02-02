class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X":10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = len(s)
        answer = dict[s[n-1]]
        for i in range(n-1):
            if dict[s[n-2-i]] >= dict[s[n-i-1]]:
                answer = answer + dict[s[n-2-i]]
            else:
                answer = answer - dict[s[n-2-i]]
        return answer