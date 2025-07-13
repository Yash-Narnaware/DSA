#Leetcode - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

#Missed the condition when given root is null.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root])
        res = []
        if not root:
            return res
        while queue:
            n = len(queue)
            lvl = []
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                lvl.append(node.val)
            res.append(lvl)

        return res


        
