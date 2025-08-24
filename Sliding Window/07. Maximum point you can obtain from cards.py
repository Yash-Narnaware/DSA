#Leetcode - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

#Consider the window of size k consisting of all elements from left/right part at start then one by one shift window from left/right to right/left and keep track of current window sum and max window sum.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        left_win_sum = sum(cardPoints[:k])
        res = left_win_sum

        l = k - 1
        r = len(cardPoints) - 1

        for i in range(k):
            left_win_sum = left_win_sum - cardPoints[l - i] + cardPoints[r - i]
            res = max(res, left_win_sum )

        return res

        
