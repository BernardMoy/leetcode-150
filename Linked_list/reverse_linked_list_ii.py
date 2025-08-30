# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Simulation
        Within the left to right section using for loop
        to assign nodes backwards to their prev pointers. 
        """
        dummy = ListNode(0, head) 
        prev = dummy 
        cur = dummy.next 

        # traverse to the point that cur is at the left position
        for _ in range(left-1): 
            prev = prev.next 
            cur = cur.next 
        
        # assign nodes backwards to their previous node within left to right range 
        for _ in range(right-left): 
            tmp = cur.next 
            cur.next = tmp.next 
            tmp.next = prev.next 
            prev.next = tmp 
        
        return dummy.next 