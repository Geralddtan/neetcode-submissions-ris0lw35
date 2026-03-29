# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = self.inOrderTraversal(root)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False

        return True            

    def inOrderTraversal(self, root):
        inorder_list = []

        def helper(root):
            if root.left:
                helper(root.left)
            inorder_list.append(root.val)
            if root.right:
                helper(root.right)

        helper(root)
        return inorder_list


