#Leetcode - https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

#similar code to search in bst just if input val > current node val and right node doesnt exist then we have to insert inut node to current node's right side, similar goes for < case.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        tmp = root
        node = TreeNode(val)

        if not tmp:
            return node

        while tmp:
            if tmp.val < val:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = node
                    return root
            else:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = node
                    return root

        
