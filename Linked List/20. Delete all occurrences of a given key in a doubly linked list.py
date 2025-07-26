#GFG - https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1

#User function Template for python3
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):

        dummy = Node(0)
        dummy.next = head
        head.prev = dummy
        
        while head:
            if head.data == x:
                head.prev.next = head.next
                if head.next:
                    head.next.prev = head.prev
            
            head = head.next
            
        return dummy.next
