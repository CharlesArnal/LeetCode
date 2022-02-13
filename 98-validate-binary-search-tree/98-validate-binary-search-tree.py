# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def analyze_tree(root):
    if root == None:
        return True, math.inf, -math.inf
    ok_left, min_left, max_left = analyze_tree(root.left)
    
    ok_right, min_right, max_right = analyze_tree(root.right)
    
    return (ok_left and ok_right and max_left<root.val and min_right>root.val ), min(root.val, min_left), max(root.val, max_right)
    
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return analyze_tree(root)[0]
        