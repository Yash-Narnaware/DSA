#Leetcode - https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        def func(i, j, cur):

            if board[i][j] != word[cur]:
                return False

            if cur == len(word) - 1:
                return True

            board[i][j] = "#"
            res = False
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx, ny = i + dx, j + dy

                if 0 <= nx < m and 0 <= ny < n:
                    res = res or func(nx, ny, cur+1)

            board[i][j] = word[cur]

            return res

        
        for i in range(m):
            for j in range(n):
                res = func(i, j, 0)

                if res:
                    return True

        return False
        
