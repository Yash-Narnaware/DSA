#Leetcode - https://leetcode.com/problems/move-zeroes/description/

#Used swap index to move all non zero elements to left of the array amd traversed the array using current pointer. whenever non zero element appears swap it with swap index and increment the swap index.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swp_idx = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                if cur != swp_idx:
                    nums[cur], nums[swp_idx] = nums[swp_idx], nums[cur]
                swp_idx += 1
