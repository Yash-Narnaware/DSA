#GFG - https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1

#Back-end complete function Template for Python 3

'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):

        cur = head
        tmp = cur.next
        
        while tmp:
            
            while tmp and tmp.data == cur.data:
                tmp = tmp.next
            if not tmp:
                break
            tmp.prev = cur
            cur.next = tmp
            cur = tmp
            tmp = tmp.next
            
        cur.next = tmp
            
        return head
