#Leetcode - https://leetcode.com/problems/find-a-peak-element-ii/description/

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            mx = 0

            for i in range(m):
                if mat[i][mid] > mx:
                    mx = mat[i][mid]
                    x, y = i, mid
            
            #Out of bounds check
            if y - 1 < 0:
                left = -1
            else:
                left = mat[x][y-1]
            
            #Out of bounds check
            if y + 1 >= n:
                right = -1
            else:
                right = mat[x][y+1] 
            
            if left < mat[x][y] > right:
                return [x, y]
            if mat[x][y] < left:
                r = mid - 1
            else:
                l = mid + 1

        
