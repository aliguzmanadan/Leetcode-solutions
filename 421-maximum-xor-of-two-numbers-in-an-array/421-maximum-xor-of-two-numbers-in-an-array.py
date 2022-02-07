#Trie class  
class xorTrie:
    """
    Number are represented in a trie, where each
    node is a digit in their binary representation
    """
    
    def __init__(self, depth):
        self.trie = {}      #trie structure
        self.depth = depth  #depth if the trie
        self.list = []      #list of all numbers in the trie 
        
    #insert a number in the trie
    def insert(self, num):
        self.list.append(num)
        trie =  self.trie
        
        for i in range(self.depth, -1, -1):
            #ith significative binary digit of num
            d = int(bool(num & 1 << i))
            if d not in trie:
                trie[d] = {}
            trie = trie[d]
            
    #Get the max XOR product betwen a given number and all possible elements in the trie
    def maxXORProduct(self, num):
        XOR = 0
        trie = self.trie
        
        for i in range(self.depth, -1, -1):
            d = int(bool(num & 1 << i))
            
            if 1-d in trie:
                trie = trie [1-d]
                XOR = (XOR << 1) + 1
            else:
                trie = trie[d]
                XOR = (XOR << 1)
        
        return XOR
                
        
    #Get the max XOR product betwwen any two elements in the trie
    def maxXOR(self):
        max_XOR = 0
        for num in self.list:
            max_XOR = max(max_XOR, self.maxXORProduct(num))
            
        return max_XOR

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        #lenght of the largest dicimal representation in nums
        depth = len(bin(max(nums)))-2
        
        #Inserting elements in the trie
        xor_trie = xorTrie(depth)
        for num in nums:
            xor_trie.insert(num)
            
        return xor_trie.maxXOR()
            
        
        