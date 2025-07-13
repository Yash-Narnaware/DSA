#Leetcode - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/

#Not difficult just a little complicated and tricky, have to keep count of row and column for each node
#created a dict for storing node values along with their row according to their columns.
#Sort priority order is column > row > node value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def func(node, row, column, res_dict):
            if not node:
                return

            if column in res_dict:
                res_dict[column].append((row, node.val))
            else:
                res_dict[column] = [(row, node.val)]

            func(node.left, row + 1, column - 1, res_dict)
            func(node.right, row + 1, column + 1, res_dict)

        res_dict = {}
        func(root, 0, 0, res_dict)
        res = sorted(res_dict.items())

        f = []
        for col, vals in res:
            vals.sort()
            f.append([j for i, j in vals])

        return f
        
