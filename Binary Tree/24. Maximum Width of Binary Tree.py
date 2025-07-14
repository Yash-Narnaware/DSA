#Leetcode - https://leetcode.com/problems/maximum-width-of-binary-tree/

#have to use the fact that for node with index i its children index will be 2*i + 1 and 2*i + 2 in 0 based indexing. so do the level order traversal and in queue while adding elements also add its index and for each level calculate the width and take max.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        queue = deque([(root, 0)])
        res = 0

        while queue:
            n = len(queue)
            res = max(res, queue[n-1][1] - queue[0][1] + 1)
            for i in range(n):
                node, idx = queue.popleft()

                if node.left:
                    queue.append((node.left, 2*idx + 1))
                if node.right:
                    queue.append((node.right, 2*idx + 2))

        return res
                

        
