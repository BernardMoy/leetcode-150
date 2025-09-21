# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ 
        use a for loop to reverse only the first k nodes, then recursively call the function to reverse the remaining nodes. 

        basic code to reverse a linked list: 
            tmp = cur.next 
            cur.next = prev 
            prev, cur = cur, tmp 
        """ 
        # if there are less than k elements left, return the head and dont reverse it 
        cur = head 
        for _ in range(k): 
            if not cur: 
                return head   
            cur = cur.next 
        
        # reverse the first k elements of the linked list 
        prev = None 
        cur = head 
        for _ in range(k): 
            tmp = cur.next 
            cur.next = prev 
            prev, cur = cur, tmp 
        
        # cur is the next element in the list 
        # head is the start element originally, prev is the start element after reverse
        # e.g. 1 -> 2 -> 3 ...  (k=2) cur = 3, head = 1, prev = 2
        # 2 -> 1  (assign head to the next recursion) 
        head.next = self.reverseKGroup(cur, k)
        return prev 