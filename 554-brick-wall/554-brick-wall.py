from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hash_map = defaultdict(int)
        
        for row in wall:
            s=0
            
            for len_brick in row[:-1]:
                s += len_brick
                hash_map[s] += + 1
                
        answer = len(wall) - max(hash_map.values(), default=0)
        return answer
        