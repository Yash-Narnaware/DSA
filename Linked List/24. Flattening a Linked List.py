#GFG - https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1


#Using heap
'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None     
'''
import heapq
class Solution:
    def flatten(self, root):

        tmp = root
        hp = []
        
        while tmp:
            hp.append((tmp.data, 0, tmp))
            tmp = tmp.next
        
        heapq.heapify(hp)
        cnt = 1
        dummy = Node(0)
        cur = dummy
        while hp:
            
            val, cnt1, node = heapq.heappop(hp)
            cur.bottom = node
            cur = cur.bottom
            
            if node.bottom:
                heapq.heappush(hp, (node.bottom.data, cnt, node.bottom))
                cnt += 1
        return dummy.bottom

      
            
