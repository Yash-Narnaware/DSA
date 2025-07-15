#Leetcode - https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

#I came up with this - 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        swp_idx = 0
        seen = set()

        for cur in range(n):
            if nums[cur] not in seen:
                seen.add(nums[cur])
                nums[cur], nums[swp_idx] = nums[swp_idx], nums[cur]
                swp_idx += 1

        return swp_idx


#But since array is sorted we dont need seen set
#much cleaner approach - keep track of swap_index and element at left of swap index will always be last unique element we placed and then compare last unique element we placed with current and do the rest.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        swp_idx = 1

        for cur in range(1, n):
            if nums[cur] != nums[swp_idx - 1]:
                nums[swp_idx] = nums[cur]
                swp_idx += 1
        return swp_idx
        
        
