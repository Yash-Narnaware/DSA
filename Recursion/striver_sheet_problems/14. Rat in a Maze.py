#GFG - https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

#Applied DFS to find all paths



class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):

        n = len(maze)
        def func(i, j, current_path, res):
            
            if i == n - 1 and j == n - 1:
                res.append(''.join(current_path))
                return
            
            maze[i][j] = 0
            #down
            if i + 1 < n and maze[i+1][j] == 1:
                current_path.append('D')
                func(i+1, j, current_path, res)
                current_path.pop()
            #left
            if j - 1 >= 0 and maze[i][j-1] == 1:
                current_path.append('L')
                func(i, j-1, current_path, res)
                current_path.pop()
            #right
            if j + 1 < n and maze[i][j+1] == 1:
                current_path.append('R')
                func(i, j+1, current_path, res)
                current_path.pop()
            #up
            if i - 1 >= 0 and maze[i-1][j] == 1:
                current_path.append('U')
                func(i-1, j, current_path, res)
                current_path.pop()
                
            maze[i][j] = 1
            
        res = []
        func(0, 0, [], res)
        
        return res
            
                    
            
            
