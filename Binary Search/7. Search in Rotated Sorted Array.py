#Leetcode - https://leetcode.com/problems/search-in-rotated-sorted-array/

#First find the rotated index then deter the boundries of search according to target value and rotated index then find the target.

#Better approach would be calculate mid if target == nums[mid] return mid then determine the sorted half using mid, l and r values. check if target is between the sorted array and change l and r bounds according to it.


class Solution:
    def search(self, nums: List[int], target: int) -> int:

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

        rot_idx = l
        #set l and r accordingly
        if rot_idx == 0:
            l = 0
            r = n - 1
        elif nums[-1] < target:
            l = 0
            r = rot_idx - 1
        else:
            l = rot_idx
            r = n - 1

        #Search the target
        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

#Better approach
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


        return -1
        
