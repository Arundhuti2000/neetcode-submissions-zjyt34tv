# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        curr_node=head
        while curr_node:
            count+=1
            curr_node=curr_node.next
        if count==n:
            return head.next
        count-=n+1
        first=head
        while (count>0):
            first=first.next
            count-=1
        first.next=first.next.next
        return head