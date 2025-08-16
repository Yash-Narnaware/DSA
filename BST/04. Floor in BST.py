#GFG - https://www.geeksforgeeks.org/problems/floor-in-bst/1

#User function Template for python3

class Solution:
    def floor(self, root, x):

        floor = -1
        while root:
            if root.data == x:
                return x
                
            if root.data > x:
                root = root.left
            else:
                floor = root.data
                root = root.right
                
        return floor
                
