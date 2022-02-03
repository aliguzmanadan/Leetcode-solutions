class TrieNode:
    """Each trie node will composed of a letter dict and the total
    """
    def __init__(self):
        self.dict = {}
        self.total =0
        


class MapSum:

    def __init__(self):
        """
        We have a map for the key-value pairs and a trie for storing all the keys and the total per character
        """
        self.trie = TrieNode()
        self.map = {}

        
    def insert(self, key: str, val: int) -> None:
        #If key already exists, the value we will be incrementing in the prefix is the 
        #difference between new and old value
        new_value = val - self.map.get(key, 0)
        self.map[key] = val
        
        #Normal insert process of a trie
        trie = self.trie
        for char in key:
            if char not in trie.dict:
                trie.dict[char] = TrieNode()
            trie = trie.dict[char]
            trie.total += new_value
        
        
    def sum(self, prefix: str) -> int:
        trie = self.trie
        for char in prefix:
            if char not in trie.dict:
                return 0
            trie = trie.dict[char]
             
        return trie.total
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)