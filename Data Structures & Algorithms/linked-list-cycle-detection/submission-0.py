# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare= head
        turtle = head
        while hare and hare.next is not None:
            turtle= turtle.next
            hare=hare.next.next
            if hare == turtle:
                return True
        return False