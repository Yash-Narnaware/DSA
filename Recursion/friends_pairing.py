#friends pairing problem - GFG - https://www.geeksforgeeks.org/problems/friends-pairing-problem5425/1&selectedLang=python3

#User function Template for python3

class Solution:
    def countFriendsPairings(self, n):
        # code here 
        
        if n == 1:
            return 1
            
        if n == 2:
            return 2
            
        return self.countFriendsPairings(n-1) + (n-1)*self.countFriendsPairings(n-2)
