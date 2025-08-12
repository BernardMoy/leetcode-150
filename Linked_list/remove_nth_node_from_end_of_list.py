# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 
        Two pointers, one fast one slow (delayed by n+1 steps)

        Linked lists can only be updated using node.next = ...
        so add a dummy node at the front
        and return head.next at the end. 
        """ 
        
        head = ListNode(0, head)
        cur1, cur2 = head, head
        
        # create a delay of n steps 
        for _ in range(n+1): 
            cur1 = cur1.next
        
        # iterate both now 
        while cur1: 
            cur1 = cur1.next
            cur2 = cur2.next
        
        # at this position, set cur2.next = cur2.next.next 
        cur2.next = cur2.next.next if cur2.next else None 

        return head.next