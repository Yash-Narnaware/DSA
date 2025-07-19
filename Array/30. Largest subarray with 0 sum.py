#GFG - https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

#Very similar to the problem of finding the number of subarrays with target sum. except here target sum is 0 and instead of freq of each sum we will store their index at which sum occurs.
#For largest subarray we just have o store the 1st occurence of particular sum beause it makes the largest possible array with sum 0 for that particular sum(0 sum subarray found when sum occurs again)

class Solution:
    def maxLength(self, arr):

        map1 = {0: -1}
        sum1 = 0
        res = 0
        for i, j in enumerate(arr):
            sum1 += j
            
            if sum1 in map1:
                res = max(res, i - map1[sum1])
            else:
                map1[sum1] = i
        
        return res
                
            
        
