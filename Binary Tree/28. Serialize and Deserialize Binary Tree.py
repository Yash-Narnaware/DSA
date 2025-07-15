#Leetcode - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

#In serialization store the tree in level order traversal and in deserialization build a tree from it

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque([root])
        res = []
      
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node == '#':
                    res.append('#')
                    continue
                else:
                    res.append(str(node.val))

                if node.left:
                    queue.append(node.left)
                else:
                    queue.append('#')
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append('#')

        return ".".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split(".")
        root = TreeNode(int(arr[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()

            if arr[i] != '#':
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i += 1

            if arr[i] != '#':
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
            i += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
