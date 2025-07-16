#GFG - https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1


#My initial approach - use set to keep track of added elements
class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):

        n1=  len(a)
        n2 = len(b)
        res = []
        seen = set()
        i, j = 0, 0
        
        while i < n1 and j < n2:
            if a[i] == b[j]:
                if a[i] not in seen:
                    seen.add(a[i])
                    res.append(a[i])
                i += 1
                j += 1
            elif a[i] > b[j]:
                if b[j] not in seen:
                    seen.add(b[j])
                    res.append(b[j])
                j += 1
            else:
                if a[i] not in seen:
                    seen.add(a[i])
                    res.append(a[i])
                i += 1
                
        while i < n1:
            if a[i] not in seen:
                seen.add(a[i])
                res.append(a[i])
            i += 1
        while j < n2:
            if b[j] not in seen:
                seen.add(b[j])
                res.append(b[j])
            j += 1
            
        return res



#Approach 2 - Uses the sorted property of lists and check the candidate elemtnt we want to insert with last appended element in result to check for duplicates

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):

        n1=  len(a)
        n2 = len(b)
        res = []
        i, j = 0, 0
        
        while i < n1 and j < n2:
            if a[i] <= b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                if not res or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
        
        while i < n1:
            if res[-1] != a[i]:
                res.append(a[i])
            i += 1
        while j < n2:
            if res[-1] != b[j]:
                res.append(b[j])
            j += 1
            
        return res
                
