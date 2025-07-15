#TUF - https://takeuforward.org/plus/dsa/problems/pre,-post,-inorder-in-one-traversal

#I done it using single pass of dfs and 3 lists, striver used the following method.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def tree_traversal(self, root):
        #your code goes here
        pre = []
        inord = []
        post = []

        queue = deque([(root, 0)])

        while queue:
            node, idx = queue.popleft()

            if idx == 0:
                pre.append(node.data)
                queue.append((node, 1))

                if node.left:
                    queue.append((node.left, 1))

            elif idx == 1:
                inord.append(node.data)
                queue.append((node, 2))

                if node.right:
                    queue.append((node.right, 1))
            
            else:
                post.append(node.data)

        return [inord, pre, post]
