# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # print(p.val)
        # print(q.val)
        def find_nodes(root,p,q):
            # print("\nstart")
            # print((root.val if root != None else -1))

            if root == None:
                # print("cas1")
                return ([],[])
            if root.val == p.val:
                # print("cas2")
                left_result = find_nodes(root.left, p, q)
                right_result = find_nodes(root.right, p ,q)
                if left_result[1] == [] and right_result[1] == []:
                    path_q = []
                else:
                    path_q = left_result[1] + right_result[1] + [root]
                return ([root],path_q)
            if root.val == q.val:
                # print("cas3")
                left_result = find_nodes(root.left, p, q)
                right_result = find_nodes(root.right, p ,q)
                if left_result[0] == [] and right_result[0] == []:
                    path_q = []
                else:
                    path_q = left_result[0] + right_result[0] + [root]
                return (path_q,[root])
            # print("cas4")
            left_result = find_nodes(root.left, p, q)
            right_result = find_nodes(root.right, p ,q)
            # print("left_result")
            # print(left_result)
            # print("right_result")
            # print(right_result)
            if left_result[0] == [] and right_result[0] == []:
                path_p = []
            else:
                    path_p = left_result[0] + right_result[0] + [root]
            if left_result[1] == [] and right_result[1] == []:
                path_q = []
            else:
                    path_q = left_result[1] + right_result[1] + [root]

            return (path_p, path_q)
        path_p, path_q = find_nodes(root, p, q)
        # print([n.val for n in path_p])
        # print([n.val for n in path_q])
        cur = root
        while True:
            # print([n.val for n in path_p])
            # print([n.val for n in path_q])
            if min(len(path_p), len(path_q)) >0 and path_p[-1] == path_q[-1]:
                cur = path_p[-1]
                path_p.pop()
                path_q.pop()
            else:
                return cur
       