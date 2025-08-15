#Leetcode - https://leetcode.com/problems/non-overlapping-intervals/description/

#Remember when it comes to overlapping - sort by start time and when it comes to non- overlapping sort by end time

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        prev = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                res += 1
            else:
                prev = intervals[i]

        
        return res
        
