#Leetcode - https://leetcode.com/problems/longest-increasing-subsequence/submissions/1662721420/

#Description - given an array find the lengest of longest incresing subsequence in it.

#One could think about sorting the original array and then taking LCS with original array but this wont work - will have problems when array contains duplicate. this method gives longest non-decreasing subsequence
#But if we find the unique elements in array and sort it and take LCS with original then it works.

#My initial approach - 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        text1 = nums
        text2 = sorted(list(set(nums)))
        m = len(nums)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]


        for i in range(1,m+1):
            for j in range(1,n+1):

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]



#Better approach - calculate longest increasing subsequence ending with index i.
#for index i+1 consider all earlier indices where element at earlier indices is < current index element that way we know that in LIS till the index we are considering we can add current index element to get even bigger LIS.
#So for each index i consider index elements < i which are smaller than element at i and LIS will be max of LIS + 1(considering LIS till all those indices)
#Make an array dp with size n = len(nums) and initialize it with 1. And at the end return the max element of this array

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)



#even better solution - O(nlogn)
#Store the tail valoues
#tail[i] = minimum possible tail value for LIS of lenght (i+1), tail -> last value in LIS
#until the array is increasing tail[i] is just as current index. In case current element less than prev tail find the correct position for current element in tail array using binary search(tail array is sorted) and place that element there
#in last the lenght of tail array is the LIS lenght.


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        def binary_search(num,arr):

            l = 0
            r = len(arr) - 1

            while l < r :
                mid = (l + r) // 2

                if tail[mid] >= num:
                    r = mid
                else:
                    l = mid + 1

            return l
            
        
        tail = [nums[0]]

        for i in range(1,len(nums)):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
            else:
                idx = binary_search(nums[i],tail)
                tail[idx] = nums[i]

        
        return len(tail)


