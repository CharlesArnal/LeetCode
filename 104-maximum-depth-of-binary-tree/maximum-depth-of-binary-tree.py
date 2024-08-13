# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # print(root)
        # print(root.left)
        # print(root.right)
        left_depth = 0 if root.left == None else self.maxDepth(root.left)
        right_depth = 0 if root.right == None else self.maxDepth(root.right)
        return 1 + max(left_depth,right_depth)
        