#GFG - https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

from typing import Optional
from collections import deque
from typing import List
"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
class Solution:
    def Paths(self, root):
        
        def func(node, cur_path, res):
            if not node.left and not node.right:
                res.append(cur_path + [node.data])
                return
            
            cur_path.append(node.data)
            if node.left:
                func(node.left, cur_path, res)
            if node.right:
                func(node.right, cur_path, res)
            cur_path.pop()
            
        res = []
        func(root, [], res)
        
        return res
        
