#GFG - https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1

#To find maximum instead of left just go right

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        
        while root.left:
            root = root.left
        return root.data
