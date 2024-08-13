# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        pivot = len(nums)//2 
        value = nums[pivot]
        left_tree = self.sortedArrayToBST(nums[:pivot])
        right_tree = self.sortedArrayToBST(nums[pivot+1:])
        return TreeNode(value, left_tree, right_tree)

        