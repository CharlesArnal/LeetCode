# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        # solution = dict()
        # def recursive(starting_pos, my_dict, my_root):
        #     if starting_pos in my_dict:
        #         my_dict[starting_pos] += [my_root.val]
        #     else:
        #         my_dict[starting_pos] = [my_root.val]
        #     if my_root.left != None:
        #         recursive(starting_pos-1, my_dict, my_root.left)
        #     if my_root.right != None:
        #         recursive(starting_pos+1, my_dict, my_root.right)
        # recursive(0, solution, root)
        # list_solution = []
        # keys = sorted(solution.keys())
        # for k in keys:
        #     list_solution.append(solution[k])
        # return list_solution
        if root == None:
            return []
        solution = dict()
        tbexp = deque([(root,0)])
        while len(tbexp) != 0:
            node, pos = tbexp.popleft()
            if pos in solution:
                solution[pos] += [node.val]
            else:
                solution[pos] = [node.val]
            if node.left != None:
                tbexp.append((node.left,pos-1))
            if node.right != None:
                tbexp.append((node.right,pos+1))
        list_solution = []
        keys = sorted(solution.keys())
        for k in keys:
            list_solution.append(solution[k])
        return list_solution

        