#Leetcode - https://leetcode.com/problems/rotate-array/description/

#Approach 1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        eff_rot = k % n

        if eff_rot != 0:
            nums[:] = nums[-eff_rot:] + nums[:n-eff_rot]


#Approach 2 - using reverse

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        eff_rot = k % n

        nums.reverse()
        nums[:eff_rot] = nums[:eff_rot][::-1]
        nums[eff_rot:] = nums[eff_rot:][::-1]
