# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Recursive function for adding two numbers
def addTwoNumRec(l1, l2, rest=0):
    
    if (l1 == None) and (l2 == None) and (rest == 0):
        return None
    
    val1 = l1.val if (l1 != None) else 0
    val2 = l2.val if (l2 != None) else 0
    next1 = l1.next if (l1 != None) else None
    next2 = l2.next if (l2 != None) else None
    
    sum = val1 + val2 + rest
    rest = sum//10
    
    return ListNode(sum % 10, addTwoNumRec(next1, next2, rest))


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            
        return addTwoNumRec(l1, l2)
            