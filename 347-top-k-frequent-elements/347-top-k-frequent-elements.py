from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        
        #Counting frequencies O(n)
        for num in nums:
            freq_dict[num] += 1
           
        #Push first k elements of the dict into the heap
        #compare the rest with the top of the heap and push them if bigger
        count = 0
        heap = []
        
        for num in freq_dict:
            if count < k:
                heappush(heap, (freq_dict[num], num))
            elif freq_dict[num] > heap[0][0]:
                heappop(heap)
                heappush(heap, (freq_dict[num], num))
            count += 1
            
        #Now k most frequent elements are in heap
        freq = [i[1] for i in heap]
        return freq
        