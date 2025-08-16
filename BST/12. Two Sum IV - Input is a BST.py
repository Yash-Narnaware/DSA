#Leetcode - https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

#done it in O(n) space. better way is to use stack same as BST iterator question

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def func(node, inorder):
            if not node:
                return 

            func(node.left, inorder)
            inorder.append(node.val)
            func(node.right, inorder)

        inorder = []
        func(root, inorder)

        l = 0
        r = len(inorder) - 1

        while l < r:
            if inorder[l] + inorder[r] == k:
                return True
            if inorder[l] + inorder[r] > k:
                r -= 1
            else:
                l += 1
        
        return False

        



