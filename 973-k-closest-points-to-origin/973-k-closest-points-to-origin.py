from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We store the closest distances to (0,0) in a heap
        heap = []
        
        #Push fisrt k points, distances to the heap
        for i in range(k):
            norm = points[i][0]**2 + points[i][1]**2
            heappush(heap, (-norm, points[i]))
            
        #Compare any other point with the top of the heap and if smaller push it in
        for i in range(k, len(points)):
            norm = points[i][0]**2 + points[i][1]**2
            if -norm > heap[0][0]:
                heappop(heap)
                heappush(heap, (-norm, points[i]))
                
        #In heap we now have the closest points
        closest_points = [i[1] for i in heap]
        return closest_points
    