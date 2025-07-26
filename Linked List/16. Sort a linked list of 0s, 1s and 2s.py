#GFG - https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

#Take 3 dummy nodes one for each element - 0, 1 and 2 and do the rest. dont forget to point end of 2 list to none as in original list last 2 can point to non terminal node in LL. Also check condition where one is not present.

'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):

        zero = Node(0)
        z1 = zero
        one = Node(0)
        o1 = one
        two = Node(0)
        t1 = two
        
        while head:
            if head.data == 0:
                z1.next = head
                z1 = z1.next
            elif head.data == 1:
                o1.next = head
                o1 = o1.next
            else:
                t1.next = head
                t1 = t1.next
            head = head.next
            

        if one.next:
            z1.next = one.next
            o1.next = two.next
        else:
            z1.next = two.next
        
        t1.next = None
        return zero.next
            
