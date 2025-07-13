#Leetcode - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

#You dont have to manually reverse levels. ust depending on whether we have to reverse the level or not predefine lvl array with zeros and add element from front or back depending on reverse or not.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root])
        res = []
        if not root:
            return res
        reverse = False

        while queue:
            n = len(queue)
            lvl = [0]*n
            for i in range(n):
                node = queue.popleft()
                #missed this clever trick - was reversing the lvls manually
                idx = i if not reverse else n - 1 - i
                lvl[idx] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(lvl)
            reverse = not reverse

        return res


        
