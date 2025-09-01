# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Maintain a front and rear linked list, 
        and add value to them depending on the current value
        iterating the head using while head: ...
        """
        
        front, rear = ListNode(), ListNode() 
        curfront, currear = front, rear

        # add nodes to front or rear depending on their values 
        while head: 
            if head.val >= x: 
                currear.next = ListNode() 
                currear = currear.next 
                currear.val = head.val
            else: 
                curfront.next = ListNode()
                curfront = curfront.next 
                curfront.val = head.val
            
            head = head.next 

        # concat front and rear   
        curfront.next = rear.next 
        return front.next