#Leetcode - https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

#Sort the preordder and now we got the inorder traversal and now we have construct the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        inorder = sorted(preorder)

        def func(preorder, inorder):
            if not inorder and not preorder:
                return None
            node = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            node.left = func(preorder[1:idx+1], inorder[:idx])
            node.right = func(preorder[idx+1:], inorder[idx+1:])

            return node
        
        return func(preorder, inorder)
        
