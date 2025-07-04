#Leetcode - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

#Find the rotated index and return the value present at it.

class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        l = 0
        r = n - 1

        #find the rotated index
        while l < r:

            mid = (l + r) // 2

            if nums[l] <= nums[mid] < nums[r]:
                r = mid - 1
            elif nums[l] > nums[mid] < nums[r]:
                r = mid
            elif nums[l] <= nums[mid] > nums[r]:
                l = mid + 1

        return nums[l]

#or another approach - modify binary search

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:

            mid = (start + end)//2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
        
