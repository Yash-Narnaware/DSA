#GFG - https://www.geeksforgeeks.org/problems/predecessor-and-successor/1

#for predecessor if current node val is less than or equal to key then update the predecessor(set current node) and move to left side. bruteforce way is to store inorder traversal and find pred and succ.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):

        succ = None
        tmp1 = root
        while tmp1:
            if tmp1.data > key:
                succ = tmp1
                tmp1 = tmp1.left
            else:
                tmp1 = tmp1.right
                
                
        pred = None
        tmp1 = root
        while tmp1:
            if tmp1.data >= key:
                tmp1 = tmp1.left
            else:
                pred = tmp1
                tmp1 = tmp1.right
                
        return [pred, succ]
                
