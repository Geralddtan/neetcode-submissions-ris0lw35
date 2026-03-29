# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Get start of second half
        slow, fast = head, head
        counter = 0
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            counter += 1
        second = slow.next
        slow.next = None

        #Reverse second half
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_reversed = prev

        #Merge first and second half
        ref = head

        while second_reversed:
            next_node = head.next
            head.next = second_reversed
            second_reversed_next = second_reversed.next
            second_reversed.next = next_node
            head = next_node
            second_reversed = second_reversed_next

        head = ref


