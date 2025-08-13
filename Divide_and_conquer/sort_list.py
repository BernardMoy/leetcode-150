# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Perform a merge sort of linked lists.

        Split the linked list into two halves using a fast and slow pointer.
        Then, merge them similar to how regular lists are merged.

        A dummy variable is useful to append to the front to produce the correct result
        (return dummy.next).
        """
        # base case
        if not head or not head.next:
            return head

        # use fast and slow pointer to split the linked list into two halves
        head = ListNode(0, head)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right = slow.next
        slow.next = None
        left = head.next

        # merge them
        new = ListNode(0, None)
        cur1 = self.sortList(left)
        cur2 = self.sortList(right)
        cur3 = new
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur3.next = cur1
                cur1 = cur1.next
            else:
                cur3.next = cur2
                cur2 = cur2.next
            cur3 = cur3.next

        if cur1:
            cur3.next = cur1
        if cur2:
            cur3.next = cur2

        return new.next
