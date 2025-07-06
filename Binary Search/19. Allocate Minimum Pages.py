#GFG - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1


class Solution:

    def findPages(self, arr, k):

        n = len(arr)
        if n < k:
            return -1
        #Helper function to check 'pages' can be valid answer or not.
        def is_pos(pages):
            
            no_of_students = 1
            cur_sum = 0
            
            for i in range(n):
                if cur_sum + arr[i] <= pages:
                    cur_sum += arr[i]
                elif arr[i] <= pages:
                    
                    cur_sum = arr[i]
                    no_of_students += 1
                    
                else:
                    return False
                    
            #Critical condition - for current no. of pages if we can allot > k student that means pages is not the minimum of max pages that can be alloted to each student bigger answer is possible.
            #If no_of_students < k which means we cant assign 'pages' to k students we tried and we could only assign 'pages' to no_of_students which is < k so have to decrease 'pages' per student.
            return no_of_students <= k
            
            
        l = max(arr)
        r = sum(arr)
        
        while l <= r:
            
            mid = (l + r) // 2
            if is_pos(mid):
                r = mid - 1
            else:
                l = mid + 1
                
        return l
                
