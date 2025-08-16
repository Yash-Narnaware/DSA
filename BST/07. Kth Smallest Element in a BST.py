#Leetcode - https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

#Remember inorder traversal gives numbers in sorted order in BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def func(node, res):

            if not node:
                return
            func(node.left, res)
            res.append(node.val)
            func(node.right, res)

        res = []
        func(root, res)

        return res[k-1]      
