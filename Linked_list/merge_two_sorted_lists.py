# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Use cur0 as a pointer for the final linked list to return, 
        and by assigning ans = cur0
        return ans returns the original linkedlist. 
        """ 

        cur0 = ListNode() 
        ans = cur0 

        cur1 = list1 
        cur2 = list2 
        while cur1 and cur2: 
            if cur1.val < cur2.val: 
                cur0.next = ListNode() 
                cur0 = cur0.next 
                cur0.val = cur1.val 
                cur1 = cur1.next
            else: 
                cur0.next = ListNode() 
                cur0 = cur0.next 
                cur0.val = cur2.val
                cur2 = cur2.next
        
        # Add the remaining ones 
        while cur1: 
            cur0.next = ListNode() 
            cur0 = cur0.next 
            cur0.val = cur1.val  
            cur1 = cur1.next 
        
        while cur2: 
            cur0.next = ListNode() 
            cur0 = cur0.next 
            cur0.val = cur2.val 
            cur2 = cur2.next

        # Scrap the first element
        return ans.next