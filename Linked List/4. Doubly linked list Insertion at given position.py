#GFG - https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        
        cnt = 0
        cur = head
        
        while cur:
            cnt += 1
            
            if cnt == p + 1:
                newNode = Node(x)
        
                newNode.prev = cur
                newNode.next = cur.next
                cur.next = newNode
                
                if newNode.next:
                    newNode.next.prev = newNode
                
                break
                
            cur = cur.next
            
        return head
        
        
            
        
        
