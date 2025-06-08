# Flood Fill

*Platform*: Leetcode | **Problem Number**: 733 | **Difficulty**: Easy  
*Category*: [Topic] | **Pattern**: [Pattern]  
*Priority*: Low

## Problem Statement
[Original Problem Link]([URL](https://leetcode.com/problems/flood-fill/description/))  
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

## Approaches
- Could be done using any traversal technique
- Just make sure each new cell you visit is in bound and has same color as starting cell then only change its color and consider visiting its neighbours.

## Solution Code
```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        m = len(image)
        n = len(image[0])

        if image[sr][sc] == color:
            return image
        
        def dfs_ff(row,col,ch):
            #base case
            if row < 0 or col < 0 or row >= m or col >= n:
                return 

            if image[row][col] == ch:
                image[row][col] = color

                dfs_ff(row+1,col,ch)
                dfs_ff(row,col+1,ch)
                dfs_ff(row-1,col,ch)
                dfs_ff(row,col-1,ch)
            else:
                return

        dfs_ff(sr,sc,image[sr][sc])
        return image
        
```

## Edge Cases
 - If starting point is already in required color then return matrix as is.
## Notes
