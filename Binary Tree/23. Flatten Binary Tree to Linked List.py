#Leetcode - https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

#Approach 1 - do preorder traversal and store the nodes in an array then connect nodes as specified in problem
#O(n) space complexity

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def dfs(node,res):

            if not node:
                return

            res.append(node)
            dfs(node.left,res)
            dfs(node.right,res)
        
        res = []
        dfs(root,res)

        for i in range(len(res)-1):
            res[i].right = res[i+1]
            res[i].left = None
        if len(res) > 0:
            res[len(res)-1].right = None
            res[len(res)-1].left = None


#Approach 2 - use stack and, postorder similar traversing
#Imagine this approach with 3 node binary tree with root node and its 2 children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if not root:
            return []
        stack = deque([root])

        while stack:
            cur = stack.pop()

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

            if stack:
                cur.right = stack[-1]
            cur.left = None 
        
