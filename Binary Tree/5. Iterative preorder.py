#Leetcode - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

#Use stack and for each node first add right then left node in stack because nature of the stack and we want to print left node first.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = deque([root])
        res = []
        if not root:
            return res

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res
        
