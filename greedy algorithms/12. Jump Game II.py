#Leetcode - https://leetcode.com/problems/jump-game-ii/description/

#solved it by myself using dp but greedy approach is to iterate through array according to steps i.e. if one step is taking us min to index l and max to idx r then iterate through l to r to find the next step range.

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l, r = 0, 0
        furthermost = 0
        steps = 0
        
        while r < len(nums) - 1:
            for i in range(l, r+1):
                furthermost = max(furthermost, i + nums[i])
            
            l = r + 1
            r = furthermost
            steps += 1

        return steps
