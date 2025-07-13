#Leetcode - https://leetcode.com/problems/diameter-of-binary-tree/description/

#For each node calculate the diameter and update it if it is > current diameter and for each node return the height to above node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diam(node, res):
            if not node:
                return 0

            left = diam(node.left, res)
            right = diam(node.right, res)

            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        res = [0]
        diam(root, res)
        return res[0]
