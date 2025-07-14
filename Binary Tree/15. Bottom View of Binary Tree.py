#GFG - https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

#Last appearing element in each column

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        
        queue = deque([(root, 0)])
        col_dict = {}
        
        while queue:
            n = len(queue)
            for _ in range(n):
                node, column = queue.popleft()
    
                col_dict[column] = node.data
                
                if node.left:
                    queue.append((node.left, column - 1))
                if node.right:
                    queue.append((node.right, column + 1))
                    
        res = sorted(col_dict.items())
        
        return [val for key, val in res]
                
                    
        
