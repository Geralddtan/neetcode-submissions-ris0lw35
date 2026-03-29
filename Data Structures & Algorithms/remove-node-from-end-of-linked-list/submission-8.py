# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        ref = head
        
        for i in range(n):
            tmp = tmp.next

        if not tmp:
            return head.next
        
        while tmp.next:
            tmp = tmp.next
            ref = ref.next
        
        ref.next = ref.next.next
        return head


