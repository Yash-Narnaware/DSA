#Leetcode - https://leetcode.com/problems/binary-search-tree-iterator/description/

#Done using O(n) space - store inorder traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.next1 = -1

        self.inorder = []

        def func(node, inorder):
            if not node:
                return 
            
            func(node.left, inorder)
            inorder.append(node.val)
            func(node.right, inorder)
        
        func(root, self.inorder)
        self.n = len(self.inorder)
        

    def next(self) -> int:
        if self.next1 == -1:
            self.next1 = 0
        else:
            self.next1 += 1
        return self.inorder[self.next1]

        
    def hasNext(self) -> bool:
        return self.next1 + 1 < self.n
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



#Can be done in O(h) space using stack

