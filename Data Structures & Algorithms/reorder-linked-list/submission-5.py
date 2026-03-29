# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            return

        node2 = slow.next
        node1 = head
        slow.next = None

        #Reverse second half
        prev = None
        while node2:
            next_node = node2.next
            node2.next = prev
            prev = node2
            node2 = next_node
        
        node2_reversed = prev

        print(node1.val)
        print(node2_reversed.val)
        #Interchange node1 and node2_reversed
        head = node1
        while node1 and node2_reversed:
            next_node1 = node1.next
            next_node2 = node2_reversed.next
            node1.next = node2_reversed
            node2_reversed.next = next_node1
            node1 = next_node1
            node2_reversed = next_node2            


