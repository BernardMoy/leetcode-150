# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ 
        Maintain a fast and slow pointer where the slow pointer has a delay of k steps. 
        Important: the slow pointer should store the value before the first element of the rotated array, 
        so that it can cut the linked list off using .next = None. 
        """ 

        # base case 
        if not head or not head.next or k == 0: 
            return head 
        
        # First find the length of the linked list so that k can be modded by n
        n = 0 
        dum = head 
        while dum: 
            dum = dum.next
            n += 1     
        k = k%n 
        if k == 0: 
            return head 

        # Maintain a fast and slow pointer 
        fast, slow = head, head 
        for _ in range(k): 
            fast = fast.next 
        
        while fast.next: 
            fast = fast.next 
            slow = slow.next 

        # cut off the slow part and set fast.next = slow part 
        ans = slow.next 
        slow.next = None 
        fast.next = head 

        return ans 
