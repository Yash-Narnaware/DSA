#GFG - https://www.geeksforgeeks.org/problems/burning-tree/1

#Find parent then perform BFS

from collections import deque
class Solution:
    def minTime(self, root, target):
        
        #find parent of each node
        parent = {}
        target_node = [0]
        def dfs(node, parent1, target_node):
            if not node:
                return 
            parent[node.data] = parent1
            
            #find target node
            if node.data == target:
                target_node[0] = node

            dfs(node.left, node, target_node)
            dfs(node.right, node, target_node)
        dfs(root, None, target_node)
        
        #BFS
        queue = deque([(target_node[0], 0)])
        visited = set()
        
        while queue:
            node, time = queue.popleft()
            visited.add(node.data)
            res = time
            
            #add unvisited neighbours to queue
            if node.left and node.left.data not in visited:
                queue.append((node.left, time + 1))
            if node.right and node.right.data not in visited:
                queue.append((node.right, time + 1))
            if parent[node.data] != None and parent[node.data].data not in visited:
                queue.append((parent[node.data], time + 1))
                
        return res
        
