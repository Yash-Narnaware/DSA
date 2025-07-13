#Leetcode - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def post(node, res):
            if not node:
                return 
            post(node.left, res)
            post(node.right, res)
            res.append(node.val)
        res = []
        post(root, res)

        return res
        
