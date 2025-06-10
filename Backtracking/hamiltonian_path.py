#gfg - https://www.geeksforgeeks.org/problems/hamiltonian-path2522/1
#A recursive function to check if hamiltonian path exists or not
#Simply from each vertex try to find hamiltonial path i.e. try to visited all node exactly once using dfs if possible then return True - path found
#After visitng all the neighbours of node remove it from visited set because there can be another way to reach that npde. so to consider that other path also remove it from visited set.
class Solution:
    def check(self, n, m, edges): 
        #code here
        
        adj = [[] for _ in range(n)]
        
        for i,j in edges:
            adj[i-1].append(j-1)
            adj[j-1].append(i-1)
            
        

        def dfs(node,count,visited,n1):
            if count == n1:
                return True
                
            visited.add(node)
            for n in adj[node]:
                if n not in visited:
                    if dfs(n,count+1,visited,n1):
                        return True
                    
                    
            visited.remove(node)
            return False
        
        
        for i in range(n):
            visited = set()
            if dfs(i,1,visited,n):
                return True
                
        return False
