#Leetcode - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


#LCA is the node of which p should be on one side and q should be on another unless they are ancestor of one another.


#My initial approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def func(node):
            if not node:
                return None


            if (node.val >= p.val and node.val <= q.val) or (node.val >= q.val and node.val <= p.val):
                return node
            
            left = func(node.left)
            right = func(node.right)

            if left:
                return left
            elif right:
                return right
            
            return None

        return func(root)
        


#Better approach - if both p and q are greater or smaller than current node value go to their side

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def func(node):
            if not node:
                return None

            if node.val < p.val and node.val < q.val:
                return func(node.right)
            if node.val > p.val and node.val > q.val:
                return func(node.left)
            
            return node
            
        return func(root)
        
