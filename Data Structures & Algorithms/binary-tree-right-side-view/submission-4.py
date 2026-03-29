# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        res = []
        if not root:
            return []
        
        while q:
            q_len = len(q)
            res.append(q[0].val)

            for i in range(q_len):
                if q[i].right:
                    q.append(q[i].right)
                if q[i].left:
                    q.append(q[i].left)

            q = q[q_len:]

        return res      


