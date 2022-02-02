from collections import deque

#Helper functions
def addToMaxQue (queue, a):
    if not queue:
        queue = deque([a])
        return queue
    elif a > queue[0]:
        queue = deque([a])
        return queue

    while a > queue[-1]:
        queue.pop()
    queue.append(a)
    return queue

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        max_que = deque()
        answer = []
        
        #Build set of ordered maximums of the first k nums
        for i in range(0,k):
            max_que = addToMaxQue(max_que, nums[i])

        #Fill in max of the first k ums
        answer.append(max_que[0])
        
        #Fill in the rest of maximums
        for i in range(k,len(nums)):
            if nums[i-k] == max_que[0]:
                max_que.popleft()
                
            max_que = addToMaxQue(max_que, nums[i])
            
            answer.append(max_que[0])
            
        return answer
            