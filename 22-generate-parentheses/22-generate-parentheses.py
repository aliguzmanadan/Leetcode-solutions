class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #cache stores the list of well-formed i pairs of parethesis, i=1,...,n
        cache = {1: ["()"]}
        
        for i in range(2, n+1):
            temp = {f"({c})" for c in cache[i-1]}
            temp1 = set()
            for j in range(1,i):
                temp1 = temp1.union({a+b for a in cache[j] for b in cache[i-j]})
            cache[i] = list(temp.union(temp1))    
            
        return cache[n]