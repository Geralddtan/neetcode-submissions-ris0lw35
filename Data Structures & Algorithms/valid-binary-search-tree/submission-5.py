# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrderTraversal(root):
            nonlocal res
            if root.left:
                inOrderTraversal(root.left)
            res.append(root.val)
            if root.right:
                inOrderTraversal(root.right)
            return res
        
        if not root:
            return True
        res = []
        inOrderTraversal(root)

        for index, val in enumerate(res):
            if index >0 and val <= res[index-1]:
                return False

        return True



            