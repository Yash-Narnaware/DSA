#Leetcode - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

#Runbinary search 2 times one time for finding first and one time for finding last.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        l = 0
        r = n - 1

        #first
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        first = l if l < n and nums[l] == target else -1

        last = -1
        l = 0
        r = n - 1

        #last
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        last = r if r >= 0 and nums[r] == target else -1

        return [first, last]
        
