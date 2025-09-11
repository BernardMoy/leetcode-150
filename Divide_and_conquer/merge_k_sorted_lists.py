# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ 
        Use a heap to add all list heads, then extract the smallest one to recreate the linked list

        The heap need to store items in the format (node.val, index, node) 
        node.val is for comparison to extract the smallest value
        index is to keep every entry distinct so that node are not compared when node.val are the same 
        node is to actually append to the answer linked list 
        """ 

        q = [] 
        heapq.heapify(q) 

        for i in range(len(lists)): 
            node = lists[i]
            if not node: 
                continue 
            heapq.heappush(q, (node.val, i, node))   # (val, index, node) 
        
        dummy = ListNode(0) 
        cur = dummy 
        while q: 
            v, i, n = heapq.heappop(q) 
            cur.next = n   # set the node itself as the next element 
            cur = cur.next 
            if n.next: 
                heapq.heappush(q, (n.next.val, i, n.next))  # push the next node back into the heap 
        
        return dummy.next 
