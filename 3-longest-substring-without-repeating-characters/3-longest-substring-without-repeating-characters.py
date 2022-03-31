class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        hashMap = {}
        maxLen = 0
        
        for j in range(len(s)):
            if s[j] not in hashMap:
                hashMap[s[j]] = j
            else:
                maxLen = max(maxLen, j-i)
                i = hashMap[s[j]] + 1
                hashMap = {key:val for key,val in hashMap.items() if val >= i}
                hashMap[s[j]] = j
                
        maxLen = max(maxLen, len(s)-i)
        
        return maxLen