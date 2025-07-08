#Leetcode - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

#determine if target present in sorted half and change the bounds according to it. just one additional condition - if nums[mid] == nums[l] == nums[r] then l += 1 and r -= 1

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[r] == nums[l]:
                l += 1
                r -= 1
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

        return False
