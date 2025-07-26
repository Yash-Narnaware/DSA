#GFG - https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1


#Approach 1: use stack
'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        
        stack = []
        tmp = head
        
        while tmp:
            stack.append(tmp)
            tmp = tmp.next
        
        carry = 1
        while stack:
            
            node = stack.pop()
            
            if node.data == 9:
                node.data = 0
                carry = 1
            else:
                node.data += carry
                carry = 0
                break
                
        if carry == 1:
            tmp = Node(1)
            tmp.next = head
            head = tmp
        return head
            

#Appraoch2: reverse the LL then do addition then reverse again

#Approach 3: use recursion - traverse till last node and add 1 to its value keep in mind if that node value is 9 then we have to return carry and set current node value to be 0

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        
        def func(node):
            if not node.next:
                if node.data == 9:
                    node.data = 0
                    return 1
                else:
                    node.data += 1
                    return 0
                    
            r1 = func(node.next)
            if r1 == 0:
                return 0
            
            if node.data != 9:
                node.data += 1
                return 0
     
            node.data = 0
            return 1
            
        r = func(head)
        
        if r == 1:
            tmp = Node(1)
            tmp.next = head
            head = tmp
        
        return head
