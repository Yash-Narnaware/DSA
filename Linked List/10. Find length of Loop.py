#GFG - https://www.geeksforgeeks.org/problems/find-length-of-loop/1

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):

        slow = head
        fast = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    
                starting = slow
                slow = slow.next
                cnt = 1
                while slow != starting:
                    cnt += 1
                    slow = slow.next
                return cnt
        return 0
                
