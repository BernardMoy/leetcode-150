# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ 
        Maintain a prev and cur pointer. 
        While cur = cur.next, skip all duplicated values and mark them 
        If marked, use prev = prev.next to delete the current, remaining single element at the end
        """ 
        if not head or not head.next: 
            return head 

        # maintain a prev and cur pointer 
        dummy = ListNode(0, head) 
        prev = dummy 
        cur = dummy.next 
        
        while cur: 
            duplicated = False 

            # if the next element has the same val as current, mark duplicated true 
            # remove all subsequent elements that are the same 
            while cur.next and cur.val == cur.next.val: 
                cur = cur.next 
                duplicated = True 
            
            # Delete the current element if a duplicate is encountered
            if duplicated: 
                prev.next = cur.next   # Delete here 
            else: 
                prev = prev.next  # Move the prev pointer 

            cur = cur.next

        return dummy.next 
