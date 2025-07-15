#Leetcode - https://leetcode.com/problems/count-complete-tree-nodes/description/

#for each node check left height(height using leftmost node) and right height(height using rightmost node) if equal then we know that subtree is full so directly return 2^height - 1 else we have to return 1 + nodes in left subtree + nodes in right subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def lh(node):
            res = 0
            while node:
                res += 1
                node = node.left
            return res
        
        def rh(node):
            res = 0
            while node:
                res += 1
                node = node.right
            return res
        
        def dfs(node):
            if not node:
                return 0

            left_height = lh(node)
            right_height = rh(node)

            if left_height == right_height:
                return 2**left_height - 1
            else:
                return 1 + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
