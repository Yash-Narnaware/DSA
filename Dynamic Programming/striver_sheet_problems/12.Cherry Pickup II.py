#Leetcode - https://leetcode.com/problems/cherry-pickup-ii/description/

#define a recursive function passing coordinates of both robots.


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        mem = {}
        def func(cur_row,r1_col,r2_col):

            if (cur_row,r1_col,r2_col) not in mem:
                if r1_col < 0 or r1_col >= cols or r2_col < 0 or r2_col >= cols:
                    mem[(cur_row,r1_col,r2_col)] = float('-inf')

                elif cur_row == rows - 1:
                    if r1_col == r2_col:
                        return grid[cur_row][r1_col]
                    else:
                        return grid[cur_row][r1_col] + grid[cur_row][r2_col]

                else:
                    res = float('-inf')
                    for i,j in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]:
                        new_col1 = r1_col + i
                        new_col2 = r2_col + j

                        if r1_col != r2_col:
                            res = max(res,func(cur_row+1,new_col1,new_col2) + grid[cur_row][r1_col] + grid[cur_row][r2_col])
                        else:
                            res = max(res,func(cur_row+1,new_col1,new_col2) + grid[cur_row][r1_col])

                    mem[(cur_row,r1_col,r2_col)] = res
            return mem[(cur_row,r1_col,r2_col)]

        return func(0,0,cols-1)



#Tabulation - wrong 
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        dp = [[[0]*cols for _ in range(rows)]*cols]
        for i in range(cols):
            for j in range(cols):
                dp[rows-1][j][i] = grid[rows-1][j]

        for i in range(rows-2,-1,-1):
            for j1 in range(cols):
                for j2 in range(cols):

                    res = float('-inf')
                    for i,j in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]:
                        new_col1 = r1_col + j1
                        new_col2 = r2_col + j2

                        if new_col1 < 0 or new_col2 < 0 or new_col1 >= cols or new_col1 >= cols:
                            continue

                        if j1 != j2:
                            res = max(res,dp[i+1][new_col1][new_col2] + grid[i][j1] + grid[i][j2])
                        else:
                            res = max(res,dp[i+1][new_col1][new_col2] + grid[i][j1])

                    dp[i][j1][j2] = res

        return dp[0][0][0] + dp[0][col-1][0]  
