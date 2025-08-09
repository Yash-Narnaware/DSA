#GFG - https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1


#sort the arrival and departure time separately. and increase the counter every time arrival time is seen in sorted array and decrease the counter when departure time is seen and return the max value of counter seen.

#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        
        arr.sort()
        dep.sort()
        
        i = 0
        j = 0
        cnt, cnt_mx = 0, 0
        
        while i < len(arr):
            if arr[i] <= dep[j]:
                cnt += 1
                i += 1
            else:
                j += 1
                cnt -= 1
            cnt_mx = max(cnt_mx, cnt)
                
        return cnt_mx
