"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = defaultdict(lambda: Node(0))
        dic[None] = None
        curr = head

        while curr:
            dic[curr].val = curr.val
            dic[curr].next = dic[curr.next]
            dic[curr].random = dic[curr.random]
            curr = curr.next

        return dic[head]
