#GFG - https://www.geeksforgeeks.org/problems/children-sum-parent/1

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        
        def func(node):
            
            if not node.left and not node.right:
                return node.data
    
            left, right = 0, 0
            if node.left:
                left = func(node.left)
            if node.right:
                right = func(node.right)
            
            if left == -1 or right == -1 or (node.data != left + right):
                return -1
            return node.data
                
        res = func(root)
        
        return 1 if res != -1 else 0
