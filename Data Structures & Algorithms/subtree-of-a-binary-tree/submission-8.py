# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot and root.val == subRoot.val:
            return self.isSametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        elif not root:
            return False
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSametree(self, root, subroot):
        if root and subroot and root.val == subroot.val:
            return True and self.isSametree(root.left, subroot.left) and self.isSametree(root.right, subroot.right)
        elif not root and not subroot:
            return True
        else:
            return False
        