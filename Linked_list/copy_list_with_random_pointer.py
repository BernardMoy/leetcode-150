"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Two passes: First generate a dict that maps old nodes to new nodes 
        Second assign the random pointers according to the mapping 
        (d[cur].random = d[cur.random])
        """

        d = {} 
        clone = ListNode()
        curclone = clone 

        cur = head 
        while cur: 
            # clone 
            curclone.next = ListNode()
            curclone = curclone.next
            curclone.val = cur.val 

            # map old node to new node 
            d[cur] = curclone 

            cur = cur.next
        
        cur = head 
        while cur: 
            if not cur.random: 
                d[cur].random = None 
            else:
                d[cur].random = d[cur.random]
            cur = cur.next 
        
        return clone.next 