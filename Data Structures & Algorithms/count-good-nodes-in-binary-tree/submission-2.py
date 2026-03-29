# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res  = 0

        def dfs(node, max_value):
            nonlocal res
            if max_value <= node.val:
                res += 1

            if node.left:
                dfs(node.left, max(max_value, node.val))
            if node.right:
                dfs(node.right, max(max_value, node.val))
            
        dfs(root, root.val)
        return res


