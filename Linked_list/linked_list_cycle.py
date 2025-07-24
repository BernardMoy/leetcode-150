# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Use a fast and slow pointer
        that are assigned head to iterate 
        if fast == slow, it has a cycle 
        """ 

        fast = head 
        slow = head 

        while fast and fast.next and fast.next.next: 
            fast = fast.next.next
            slow = slow.next 

            # If fast = slow at any point, it loops 
            if fast == slow: 
                return True 
            
        return False