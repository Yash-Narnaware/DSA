#Leetcode - https://leetcode.com/problems/symmetric-tree/description/

#Checking if right part of left subtree is equal to left part of right subtree and vice versa

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        #Checking if right part of left subtree is equal to left part of right subtree and vice versa
        def func(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 or not node2) or node1.val != node2.val:
                return False
            
            r1 = func(node1.left, node2.right)
            r2 = func(node1.right, node2.left)

            return r1 and r2

        return func(root.left, root.right)

        
