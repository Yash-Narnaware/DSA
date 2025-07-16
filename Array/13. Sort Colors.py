#Leetcode - https://leetcode.com/problems/sort-colors/description/


#Approach 1 - in one pass count the frequencies of 0, 1 and 2 and then rearrange the array according to it.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0,0,0] 
        for i in nums:
            count[i] += 1

        for i in range(count[0]):
            nums[i] = 0
        for i in range(count[0],count[0]+count[1]):
            nums[i] = 1
        for i in range(count[0]+count[1],len(nums)):
            nums[i] = 2


#Approach 2 - Dutch natioal flag algorithm - have 3 pointers low - at 1st index, high - at last index and mid traversing from 0 till its less than or equal to high.
#if number at mid is 0 then swap it with low and increase low as well as mid, if mid element is 1 just move on to next, if it is 2 then swap it with high and decrement high by 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low, mid = 0, 0
        high = n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1
