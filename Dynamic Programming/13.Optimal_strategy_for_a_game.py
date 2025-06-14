#GFG - https://www.geeksforgeeks.org/problems/optimal-strategy-for-a-game-1587115620/1

#while writing recersion think from your point of view like what would you have after opponent takes any decision.
#we have to return the maximum possible value we can get
#If problem asked for a always winning strategy then since we are playing first - we can always get odd numbered values or even numbered values. so calculate the sum of odd and even indices separately and always get those indices to win the game.



#Recursive solution

class Solution:
    def maximumAmount(self, arr):
        
        def func(i,j):
            #Adjecent cells
            if i+1 == j:
                return max(arr[i],arr[j])

            #Considering choosing first and last element and then after opponent taking move choosing min from opponents options cause opponent plays optimally and from our POV we have to choose min from opponents options
            return max(
                arr[i] + min(func(i+2,j),func(i+1,j-1)),
                arr[j] + min(func(i+1,j-1),func(i,j-2))
                )
            
        
        return func(0,len(arr)-1)



#Memoization - Top down
class Solution:
    def maximumAmount(self, arr):
        # code here
        
        mem = {}
        def func(i,j):
            
            if (i,j) not in mem:
                if i+1 == j:
                    mem[(i,j)] = max(arr[i],arr[j])
                else:
                
                    mem[(i,j)] = max(
                        arr[i] + min(func(i+2,j),func(i+1,j-1)),
                        arr[j] + min(func(i+1,j-1),func(i,j-2))
                        )
                    
            return mem[(i,j)]
                
        
        return func(0,len(arr)-1)



#Tabulation - bottom up
#please watch video again
