# Surrounded Regions

*Platform*: Leetcode | **Problem Number**: 130 | **Difficulty**: Medium  
*Category*: [Topic] | **Pattern**: [Pattern]  
*Priority*: Medium

## Problem Statement
[Original Problem Link]([URL](https://leetcode.com/problems/surrounded-regions/description/))  
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every 'O' cell.
- Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

## Approaches

- Multi source BFS problem can be done using DFS
- Traverse the grid and add all the 'O' on the boundry to the queue
- Perform BFS from and add each reachable cell from them to do not change list
- Traverse grid again and change all the 'O' to 'X' which are not in do ot change list

## Solution Code
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()
        m = len(board)
        n = len(board[0])
        donotchange = set()
        visited = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or i == m-1 or j == 0 or j == n-1):
                    queue.append((i,j))
                    donotchange.add((i,j))

        while queue:
            a,b = queue.popleft()

            for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                nx = a + dx
                ny = b + dy

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O' and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny))
                    donotchange.add((nx,ny))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in donotchange:
                    board[i][j] = 'X'
                    
```

## Edge Cases

## Notes
