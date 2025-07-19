#GFG - https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

#Approach 1: I came up with it
class Solution:
    def findTwoElement(self, arr):
        
        n = len(arr)
        arr_sum = sum(arr)
        true_sum = (n * (n + 1)) // 2
        
        seen = set()
        
        for i in arr:
            if i in seen:
                repeted = i
                break
            else:
                seen.add(i)
        
        return [repeted, true_sum - arr_sum + repeted]
        
        

#Constant space approach - use square sum formula along with sum formula to get 2 equations in terms of missing and repeating numbes and then solve it

class Solution:
    def findTwoElement(self, arr):
        
        n = len(arr)
        true_sum = (n * (n + 1)) // 2
        true_sqr_sum = (n * (n+1) * (2*n + 1)) // 6
        arr_sum = 0
        sqr_sum = 0
        
        for i in arr:
            arr_sum += i
            sqr_sum += i*i
        
        t1 = true_sqr_sum - sqr_sum
        t2 = true_sum - arr_sum
        
        missing = ((t1/t2) + t2) // 2
        
        return [int(missing - t2), int(missing)]
        
        


