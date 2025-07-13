#GFG - https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

#for left go extreme left then if no left possible go right then again go let till no left possible do this till first leaf node appears. same for right boundry just swap left with right
# calculating bottom boundry is straightforward
#Keep in mind the edge case of having single node

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def boundaryTraversal(self, root):

        if not root:
            return []
        if not root.left and not root.right:
            return [root.data]
        
        #left boundry
        left = []
        node = root.left
        while node and (node.left or node.right):
            left.append(node.data)
            if node.left:
                node = node.left
            else:
                node = node.right
                
        #Right boundry
        right = []
        node = root.right
        while node and (node.left or node.right):
            right.append(node.data)
            if node.right:
                node = node.right
            else:
                node = node.left
        
        #leaves
        leaves1 = []
        def leaves(node, res):
            if not node.left and not node.right:
                res.append(node.data)
            
            if node.left:
                leaves(node.left, res)
            if node.right:
                leaves(node.right, res)
                
        leaves(root, leaves1)
        
        return [root.data] + left + leaves1 + right[::-1]
