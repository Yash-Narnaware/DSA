#Leetcode - https://leetcode.com/problems/merge-intervals/description/

#Sort the intervals by start time and iterate through intervals and keep merging current interval with prev till it intersects else add it to res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        res = []

        for i in range(1, len(intervals)):

            if intervals[i][0] <= prev[1]:
                prev = [prev[0], max(prev[1], intervals[i][1])]
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)
        return res
        
