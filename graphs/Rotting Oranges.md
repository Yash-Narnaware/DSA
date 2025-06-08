# Rotting Oranges

*Platform*: Leetcode | **Problem Number**: 994 | **Difficulty**: Medium  
*Category*: Graph Traversal | **Pattern**: Multi source BFS  
*Priority*: Medium

## Problem Statement
[Original Problem Link](https://leetcode.com/problems/rotting-oranges/description/)  
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Approaches

- It is multi-source BFS problem.
- Add all the rotten oranges present in grid at start to queue - equivant of starting BFS from multiple points
- Keep visited set and only traverse to all the fresh oranges
- Each time you add something to queue along with it add time+1 and final time will be maximum of all the time we calculated for each orange rotting.

## Solution Code
``` python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        m = len(grid)
        n = len(grid[0])
        fresh_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0
        if len(queue) == 0:
            return -1
        

        time = 0
        while queue:
            a,b,c = queue.popleft()
            time = max(time,c)

            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx = a + dx
                ny = b + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    queue.append((nx,ny,c+1))

        if fresh_oranges != 0:
            return -1  

        return time

        
```

## Edge Cases
 - Count all the fresh oranges in a grid if none then return 0
 - Count all the rotten oranges at start if none return 0
## Notes
- After BFS if number of fresh oranges is none zero return -1
