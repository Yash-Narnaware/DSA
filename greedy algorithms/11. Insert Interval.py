#Leetcode - https://leetcode.com/problems/insert-interval/description/

#iterate through all intervals check for non overlapping cases newinterval entirely comes before currnt interval or newinterval comes entirely after current interval. if they intersect then merge them and set this merges interval as new interval.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        i = 0

        # for start, end in intervals:
        while i < len(intervals):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            else:
         
                temp_start = min(intervals[i][0], newInterval[0])
                temp_end = max(intervals[i][1], newInterval[1])

                newInterval = [temp_start, temp_end]

            i += 1

        res.append(newInterval)

        return res
