#GFG - https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

#Sort the meetings according to their end time and keep adding non overlapping meetings.

class Solution:
    
    def maximumMeetings(self,start,end):

        tmp = []
        
        for i in range(len(start)):
            tmp.append([start[i], end[i]])
            
        tmp.sort(key=lambda x: x[1])

        res = 1
        cur = 0
        
        for i in range(1, len(tmp)):
            if tmp[i][0] > tmp[cur][1]:
                res += 1
                cur = i
        
        return res
        
