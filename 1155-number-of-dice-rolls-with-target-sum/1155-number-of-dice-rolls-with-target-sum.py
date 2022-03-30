class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target > n*k:
            return 0
        
        t = target
        #Initializig dict that will store the values for (j,k,t-l) 
        dynamic_dict = {}
        for i in range(t-(n-1)*k, t-n+2):
            dynamic_dict[(1,k,i)] = 0 if (k<i or i<=0) else 1
            
        #Changing dict for each iteration
        for j in range(2, n):
            temp_dict = dynamic_dict.copy()
            dynamic_dict.clear()
            for i in range(t-(n-j)*k, t-n+j+1):
                dynamic_dict[(j,k,i)] = 0
                for l in range(1,k+1):
                    dynamic_dict[(j,k,i)] += temp_dict[(j-1, k, i-l)]
                dynamic_dict[(j,k,i)] %= 1000000007
                
        #Compute final answer
        
        return sum(dynamic_dict.values()) % 1000000007
        
        