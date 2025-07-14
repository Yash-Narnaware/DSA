#Leetcode - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

#if p or q found return that node and for any node if we are not returning null from both pats then return that node as LCA.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def LCA(node):
            if not node or node == p or node == q:
                return node
            
            left = LCA(node.left)
            right = LCA(node.right)

            if not left:
                return right
            
            elif not right:
                return left

            else:
                return node

        return LCA(root)


        
