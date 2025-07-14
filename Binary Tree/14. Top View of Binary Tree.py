#GFG - https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

#Use level order traversal with columns concept and from each column we have to pick element with lowest row(in other words first appearce of element belongiging to that column)

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
from collections import deque
class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):

        queue = deque([(root, 0)])
        clm_dict = {}
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                node, column = queue.popleft()
                
                if column not in clm_dict:
                    clm_dict[column] = node.data
                
                if node.left:
                    queue.append((node.left, column - 1))
                if node.right:
                    queue.append((node.right, column + 1))
                    
        res = sorted(clm_dict.items())
        
        return [val for key, val in res]
                    
                
