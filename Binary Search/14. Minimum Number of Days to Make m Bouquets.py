#Leetcode - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:


        n = len(bloomDay)
        def calc_bouquets(days):
            
            l = 0
            r = 0

            res = 0
            while r < n:
                if bloomDay[r] - days <= 0:
                    r += 1
                else:
                    r += 1
                    l = r
                if r - l == k:
                    res += 1
                    l = r

            return res

        l = 1
        r = max(bloomDay)

        while l <= r:
            mid = (l + r) // 2
            if calc_bouquets(mid) >= m:
                r = mid - 1
            else:
                l = mid + 1

        return l if l <= max(bloomDay) else -1
        
