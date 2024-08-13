# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def subfunction(a,b):
            if a>b:
                return [None]
            if a==b:
                return [TreeNode(a)]
            all_options = []
            for i in range(a,b+1):
                left_options = subfunction(a,i-1)
                right_options = subfunction(i+1,b)
                for option_1 in left_options:
                    for option_2 in right_options:
                        all_options.append(TreeNode(i,option_1,option_2))
            return all_options
        return subfunction(1,n)


