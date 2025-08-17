#Leetcode - https://leetcode.com/problems/recover-binary-search-tree/description/

#there can be 2 spots where elements are not sorted(or 1 if we interchanged the adjecent elements). find them during inorder traversal and after inorder traversal swap their values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = [TreeNode(float('-inf'))]
        last = [None]
        first = [None]
        middle = [None]

        def func(node, prev, first, last, middle):

            if not node:
                return 

            func(node.left, prev, first, last, middle)

            if prev[0] and node.val < prev[0].val:

                if not first[0]:
                    first[0] = prev[0]
                    middle[0] = node
                else:
                    last[0] = node
            prev[0] = node
            func(node.right, prev, first, last, middle)

        func(root, prev, first, last, middle)

        if first[0] and last[0]:
            first[0].val, last[0].val = last[0].val, first[0].val
        elif first[0] and middle[0]:
            first[0].val, middle[0].val = middle[0].val, first[0].val


        
