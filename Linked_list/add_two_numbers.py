# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Maintain a carry variable. 
        Iterate both while both l1 and l2 pointer values are present 
        and at the end, add the remaining values from either one of them and dont forget to add the carry after that. 
        """

        ans = ListNode()
        cur = ans 
        carry = 0 

        # Iterate l1 and l2 while both values are present 
        while l1 and l2: 
            digit = (l1.val + l2.val + carry)%10
            carry = (l1.val + l2.val + carry)//10
            cur.next = ListNode(digit) 
            cur = cur.next 

            l1 = l1.next 
            l2 = l2.next 
        
        # After that, add the remaining values either from l1 or l2 
        while l1: 
            digit = (l1.val + carry)%10
            carry = (l1.val + carry)//10
            cur.next = ListNode(digit) 
            cur = cur.next 
            l1 = l1.next 

        while l2: 
            digit = (l2.val + carry)%10
            carry = (l2.val + carry)//10
            cur.next = ListNode(digit) 
            cur = cur.next 
            l2 = l2.next   
        
        # Finally, add the carry (e.g. 999+999 -> 1 carry at the end)
        if carry: 
            cur.next = ListNode(carry) 
            cur = cur.next 

        return ans.next 