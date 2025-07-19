#Leetcode - https://leetcode.com/problems/next-permutation/description/

#From right find 1st element which is not in increasing order because if they are in increasing then we cant find the next permutation. next swap that element with just next bigger element that it. then sort the reverse sorted array from right side of index using 2 pointers(array will be reverse sorted since we found index such that from right sie till that index array is increasing)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        #Find the index to replace
        found = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                found = i
                break
        if found == -1:
            return nums.reverse()
        
        for i in range(n-1, found, -1):
            if nums[i] > nums[found]:
                nums[found], nums[i] = nums[i], nums[found]
                break
        
        l = found + 1
        r = n - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


        
