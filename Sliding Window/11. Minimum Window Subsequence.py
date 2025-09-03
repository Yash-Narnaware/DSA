#GFG - https://www.geeksforgeeks.org/problems/minimum-window-subsequence/1

#Very weird question - take 2 ptrs and traverse in s1 till we find each element from s2 then traverse back till we find all elements backwards from s2 and then calculate the window size

class Solution:
    def minWindow(self, s1, s2):
        # Code here
        
        p1 = 0
        p2 = 0
        res = float('inf')
        res_str = ""
        
        while p1 < len(s1):
            
            if s1[p1] == s2[p2]:
                p2 += 1
                
                if p2 == len(s2):

                    end = p1 + 1
                    p2 -= 1
                    
                    while p2 >= 0:
                        if s1[p1] == s2[p2]:
                            p2 -= 1
                        p1 -= 1
                    p1 += 1
                    p2 += 1
                    
                    if res > end - p1:
                        res = end - p1
                        res_str = s1[p1:end]

            p1 += 1
            
        return res_str
            
        
