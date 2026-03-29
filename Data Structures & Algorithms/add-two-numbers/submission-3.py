# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry_forward = 0
        while l1 or l2:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            val = val_1 + val_2 + carry_forward
            carry_forward = 1 if val > 9 else 0
            remainder = val%10
            dummy.next = ListNode(remainder)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            dummy = dummy.next

        if carry_forward:
            dummy.next = ListNode(carry_forward)
        
        return head.next
