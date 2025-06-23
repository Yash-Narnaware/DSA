#Leetcode - https://leetcode.com/problems/largest-divisible-subset/

#Similar code structure as LIS just instead of checking j th element is smaller or not check %.
#for calculating dp[i] check all the prev indices for if nums[j] % nums[i] == 0 or nums[i] % nums[j] == 0 if yes then ans is dp[i] = dp[j] + 1

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1]*n
        nums.sort()
        
        temp = [i for i in range(n)]
    
        max1 = 0
        for i in range(1,n):
            for j in range(i):
                if nums[j] % nums[i] == 0 or nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        temp[i] = j
                        
            if dp[i] > dp[max1]:
                max1 = i
                        
        idx = dp[max1] - 1
        lis = [0]*dp[max1]
        while idx >= 0:
            lis[idx] = nums[max1]
            max1 = temp[max1]
            idx -= 1
    
        return lis
        
