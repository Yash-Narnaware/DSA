#Leetcode - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

#dont overthink - just calculate parent of each node so that we can perform BFS from target node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        #find parent of each node
        parent = {}
        def dfs(node, parent1):
            if not node:
                return 
            parent[node.val] = parent1

            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        #Perform BFS from target node
        queue = deque([(target, 0)])
        visited = set()
        res = []
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                res.append(node.val)
                continue
            visited.add(node.val)
            
            #add unvisited neighbours to queue
            if node.left and node.left.val not in visited:
                queue.append((node.left, dist + 1))
            if node.right and node.right.val not in visited:
                queue.append((node.right, dist + 1)) 

            if parent[node.val] != None and parent[node.val].val not in visited:
                queue.append((parent[node.val], dist + 1))

        return res
            

        
