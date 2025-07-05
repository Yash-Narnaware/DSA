#Leetcode - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def calc_days(capacity):

            days = 0
            sum1 = 0
            for i in weights:
                sum1 += i
                if sum1 >= capacity:
                    days += 1
                    if sum1 == capacity:
                        sum1 = 0
                    else:
                        sum1 = i

            return days + 1 if sum1 > 0 else days

        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2
            if calc_days(mid) <= days:
                print("yes")
                r = mid - 1
            else:
                l = mid + 1

        return l
