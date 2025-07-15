#Letcode - https://leetcode.com/problems/binary-tree-inorder-traversal/description/

#use stack and keep adding node and going left till left is not possible then pop top element and add it to res then go to right side of that node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = deque([])
        res = []
        if not root:
            return res

        node = root
        while node or stack:

            while node:
                stack.append(node)
                node = node.left

            if not stack:
                break
            node = stack.pop()
            res.append(node.val)

            node = node.right

        return res
        
