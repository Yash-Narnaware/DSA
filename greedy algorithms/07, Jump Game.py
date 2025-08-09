#Leetcode - https://leetcode.com/problems/jump-game/description/

#Keep track of max reachable index while traversing the array and when 0 occurs it should be greater than zeros index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reachable_idx = 0
        if len(nums) == 1: return True

        for i, j in enumerate(nums):
            if i == len(nums) - 1:
                return True
            if j == 0:
                if max_reachable_idx <= i:
                    return False
            max_reachable_idx = max(max_reachable_idx, i + j)



#Even better and clean way - while traversing at any index max reachable index should be >= current index else return False

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reachable_idx = 0
        
        for i, j in enumerate(nums):
            if i > max_reachable_idx:
                return False
            max_reachable_idx = max(max_reachable_idx, i + j)
        
        return True
