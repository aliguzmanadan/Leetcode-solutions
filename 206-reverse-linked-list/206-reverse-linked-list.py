# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Function reverting the list and returning head and tail of this list
def head_tail_reverse(node):
    if node is None:
        return None, None
    if node.next is None:
        return node, node
    
    head, tail = head_tail_reverse(node.next)
    node.next = None
    tail.next = node
    return head, node
        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head, _ = head_tail_reverse(head)
        return head
        
        