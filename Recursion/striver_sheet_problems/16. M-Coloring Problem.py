#GFG - https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1

#Try all colors at all nodes. - write recursive dfs function which calls func on next node(index+1) if we found valid color for current node.


class Solution:
    def graphColoring(self, v, edges, m):
    
        if m >= v:
            return True
            
        adj = [[] for _ in range(v)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        visited = [-1]*v
        
        def can_color(node, color):
            for n in adj[node]:
                if visited[n] == color:
                    return False
            return True
        
        def dfs(node, visited):
            
            if node == v:
                return True
                
            for color in range(m):
                if can_color(node, color):
                    visited[node] = color
                    r = dfs(node+1, visited)
                    if r:
                        return True
                    visited[node] = -1
             
            return False 
            
        return dfs(0, visited)
                    
            
        
        
        
                    
