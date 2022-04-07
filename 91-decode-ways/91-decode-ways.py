class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]== '0':
            return 0
        
        #Cache stores the ansewres for the substrings [:i], and [:i+1], with i = 0, n-1
        cache = [1,1]
        
        for i in range(1, len(s)):
            temp = 0
            
            #compute the numDecodings for s[:i+1]
            if s[i] != '0':
                temp += cache[1]
            if int(s[i-1:i+1]) in range(10,27):
                temp += cache[0]
                
            #update cache
            cache[0] = cache[1]
            cache[1] = temp
            
        return cache[1]
        