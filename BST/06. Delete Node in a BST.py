#Leetcode - https://leetcode.com/problems/delete-node-in-a-bst/description/

#Find the node and replace it with right subtree and put the left subtree of the node in right subtree's leftmost part as we know all the elements in left subtree will be less than right subtree elements. reverse can be done i.e. replace found node with left subtree and put right subtree to rightmost part of left subtree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def func(node, key):
            if not node:
                return None
            if node.val == key:
                if node.right:
                    tmp = node.right
                    while tmp.left:
                        tmp = tmp.left
                    tmp.left = node.left

                    return node.right
                else:
                    return node.left

            if key < node.val:
                node.left = func(node.left, key)
            else:
                node.right = func(node.right, key)
            
            return node

        return func(root, key)
        
