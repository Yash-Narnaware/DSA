#GFG - https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

from typing import Optional
from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        
        tail = head
        res = []
        if not head:
            return res

        while tail.next:
            tail = tail.next
        
        while head.data < tail.data:
            
            val = head.data + tail.data
            
            if val == target:
                res.append([head.data, tail.data])
                head = head.next
                tail = tail.prev
            elif val > target:
                tail = tail.prev
            else:
                head = head.next
                
        return res
