#Leetcode - https://leetcode.com/problems/binary-tree-right-side-view/

# right side view - last element from each level(adding nodes left then right)
# left side view -  last element from each level(adding nodes right then left)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #Last element from each level
        queue = deque([root])
        res = []

        if not root:
            return res

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(node.val)
        
        return res
        
