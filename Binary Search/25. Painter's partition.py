#GFG - https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1

#binary search on answers - for a time check if job can be finished by k or less painters if yes then try to decrease time and chaeck again.

class Solution:
    def minTime (self, arr, k):

        #Helper function to check if job can be done in time time1 by atmost k painters
        def is_pos(time1):
            
            cur_sum = 0
            min_painters_needed = 0
            for i in arr:
                cur_sum += i
                
                if cur_sum == time1:
                    min_painters_needed += 1
                    cur_sum = 0
                elif cur_sum > time1:
                    min_painters_needed += 1
                    cur_sum = i
            
            if cur_sum != 0:
                min_painters_needed += 1
                
            return min_painters_needed <= k
                
        n = len(arr)
        l = max(arr)
        r = sum(arr)
        
        while l <= r:
            
            mid = (l + r) // 2
            
            if is_pos(mid):
                r = mid - 1
            else:
                l = mid + 1
                
        return l
        
