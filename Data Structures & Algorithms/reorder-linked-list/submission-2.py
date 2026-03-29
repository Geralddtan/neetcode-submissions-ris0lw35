# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse second half
        curr = slow.next
        prev = None
        slow.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        #Reorder
        first = head
        second = prev

        while second:
            next_node_first = first.next
            next_node_second = second.next
            first.next = second
            second.next = next_node_first
            first, second = next_node_first, next_node_second


