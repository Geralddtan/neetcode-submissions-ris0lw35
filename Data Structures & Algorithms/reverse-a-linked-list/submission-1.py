# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        tmp = None
        while node:
            next_node = node.next
            node.next = tmp
            tmp = node
            node = next_node
        return tmp

