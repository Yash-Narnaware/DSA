#GFG - https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1

class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        
        unique_elems = set(arr)
        seen = set()
        res = 1
        
        for i in arr:
            if i not in seen:
                seen.add(i)
                lenght = 1
                
                tmp1 = i - 1
                while tmp1 in unique_elems:
                    seen.add(tmp1)
                    lenght += 1
                    tmp1 -= 1
                
                tmp2 = i + 1
                while tmp2 in unique_elems:
                    seen.add(tmp2)
                    lenght += 1
                    tmp2 += 1
                    
                res = max(res, lenght)
                
        return res
                
                
