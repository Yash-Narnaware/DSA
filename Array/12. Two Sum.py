#Leetcode - https://leetcode.com/problems/two-sum/description/

#Use hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        idx_dict = {}

        for i, j in enumerate(nums):
            idx_dict[j] = i

        for i in range(n):
            find = target - nums[i]
            if find in idx_dict and idx_dict[find] != i:
                return [i, idx_dict[find]]
        
