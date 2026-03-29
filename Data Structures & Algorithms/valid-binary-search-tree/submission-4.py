# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        
        def inOrderTraversal(root):
            nonlocal res

            if root.left:
                inOrderTraversal(root.left)
            res.append(root.val)
            if root.right:
                inOrderTraversal(root.right)
            
        inOrderTraversal(root)
        for key, value in enumerate(res):
            if key > 0 and value <= res[key-1]:
                return False
        return True
        

