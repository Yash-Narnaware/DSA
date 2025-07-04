#Leetcode - https://leetcode.com/problems/single-element-in-a-sorted-array/description/

#Just decide where to go on basis of where other element same as mid exists(left or right) and current index position.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:

            mid = (l + r) // 2

            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                if mid % 2 == 0:
                    r = mid - 2
                else:
                    l = mid + 1

            elif mid + 1 < n and nums[mid + 1] == nums[mid]:
                if mid % 2 == 0:
                    l = mid + 2
                else:   
                    r = mid - 1

            else:
                return nums[mid]
