#Leetcode - https://leetcode.com/problems/merge-intervals/description/

#Sort by start and then merging can be done in one pass.
#If sorted by end then we will fail to merge in one pass.
#e.g - intervals = [[3,4],[5,6],[7,8],[1,10]]

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
        
