#GFG - https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1

#calculate LIS as usual while calculating it keep track of previous element in LIS for each index. like dp[i] is the lenght of LIS ending with nums[i] so keep track of previous element in LIS of nums[i].
##Construct LIS by finding max in dp array then add it to lis then move to 'parent' of that element.


class Solution:
    def getLIS(self, arr):

        n = len(arr)
        dp = [1]*n
        
        temp = [i for i in range(n)]
    
        max1 = 0
        for i in range(1,n):
            for j in range(i):
                if arr[j] < arr[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        temp[i] = j
                        
            if dp[i] > dp[max1]:
                max1 = i
                        
        idx = dp[max1] - 1
        lis = [0]*dp[max1]
        while idx >= 0:
            lis[idx] = arr[max1]
            max1 = temp[max1]
            idx -= 1
    
        return lis
