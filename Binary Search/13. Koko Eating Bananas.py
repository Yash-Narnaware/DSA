#Leetcode - https://leetcode.com/problems/koko-eating-bananas/description/

#Define a helper function to calculate the time taken to eat all bananas for a particular k.
#set l = 1 and r = max possible value of k
#Then do the binary search on k's

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #Helper function to calculate the time taken for particular k
        def cal_time(k):
            res = 0
            for i in piles:
                res += ceil(i / k)
            return res

        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            if cal_time(mid) <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l
