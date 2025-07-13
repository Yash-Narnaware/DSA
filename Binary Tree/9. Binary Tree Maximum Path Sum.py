#Leetcode - https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

#for each node calculate the path sum as path passing through that node and change the max sum if that path sum > max_sum and for each node return max path sum till that node(return 0 if it is -ve since no point in returning -ve value)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def max_sum(node, res):
            if not node:
                return 0
            
            left = max_sum(node.left, res)
            right = max_sum(node.right, res)

            res[0] = max(res[0], node.val + left + right)

            return max(0, node.val + max(left, right))

        res = [float('-inf')]
        max_sum(root, res)

        return res[0]
