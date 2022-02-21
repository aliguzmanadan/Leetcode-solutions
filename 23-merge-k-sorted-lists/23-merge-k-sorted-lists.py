# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #initialize heap with the tuples of the form (smallest elements of each list, index of the list)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
                
        #If lists was empty return none
        if len(heap) == 0:
            return None
        
        #Initialize answer and update heap
        val, idx = heappop(heap)
        answer = ListNode(val)
        lastNode = answer
        if lists[idx]:
                heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
                
        #Get elements in order from the heap
        while heap:
            val, idx = heappop(heap)
            lastNode.next = ListNode(val)
            lastNode = lastNode.next
            if lists[idx]:
                heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
                
        return answer