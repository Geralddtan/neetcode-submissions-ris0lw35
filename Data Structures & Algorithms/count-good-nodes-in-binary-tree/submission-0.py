# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def helper(root, max_val):

            if not root:
                return

            nonlocal res

            if root.val >= max_val:
                res += 1
            
            helper(root.left, max(max_val, root.val))
            helper(root.right, max(max_val, root.val))

        helper(root, root.val)
        return res

