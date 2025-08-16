#GFG - https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1

#Do normal BST traversal and whenever node val is greater than inp update ceil

''' class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None '''
        
class Solution:
    def findCeil(self,root, inp):
        # code here
        
        ceil = -1
        while root:
            if root.key == inp:
                return inp
                
            if root.key < inp:
                root = root.right
            else:
                ceil = root.key
                root = root.left
                
        return ceil
                
