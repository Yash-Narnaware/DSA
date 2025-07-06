#GFG - https://www.geeksforgeeks.org/problems/aggressive-cows/1


class Solution:
    def aggressiveCows(self, stalls, k):

        stalls.sort()
        n = len(stalls)
        
        #Helper function to check if k1 separation between cows is possible or not.
        def is_pos(k1):
            
            cur = 0
            #Placed cow at lowest stall
            cow_count = 1
            
            i = 1
            while i < n:
                if stalls[i] - stalls[cur] >= k1:
                    cow_count += 1
                    cur = i
                
                if cow_count == k:
                    return True
                    
                i += 1
                
            return False
            
        
        l = 1
        r = 10**8
        
        while l <= r:
            
            mid = (l + r) // 2
            
            if is_pos(mid):
                l = mid + 1
            else:
                r = mid - 1
                
        return r
            
            

