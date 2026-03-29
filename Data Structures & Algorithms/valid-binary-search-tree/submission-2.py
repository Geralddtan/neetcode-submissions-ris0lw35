# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = self.inordertraversal(root)
        print(inorder)
        if len(inorder) != len(set(inorder)):
            return False
        
        # Must be increasing order
        for key, value in enumerate(inorder):
            if key > 0:
                if value <= inorder[key-1]:
                    return False
        
        return True

    def inordertraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root.left:
            self.helper(root.left, res)
        res.append(root.val)
        if root.right:
            self.helper(root.right, res)
        return res


