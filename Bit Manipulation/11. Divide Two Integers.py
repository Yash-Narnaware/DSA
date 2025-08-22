#Leetcode - https://leetcode.com/problems/divide-two-integers/description/

#At a point remove the max that is multiple of divisor from divident and update the dividend and answer according to it.


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        neg = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg = True 

        dividend = abs(dividend)
        divisor = abs(divisor)
        
        ans = 0
        while dividend >= divisor:
            cnt = 0
            while divisor * 1 << (cnt+1) < dividend:
                cnt += 1
            ans += 1 << cnt
            dividend -= divisor * 1 << cnt

        if not neg:
            ans = min(ans, 2**31 - 1)
        return -ans if neg else ans
        
