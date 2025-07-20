#Leetcode - https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head

        while True:
            if not fast or fast.next == None:
                return slow
            slow = slow.next
            fast = fast.next.next
            
            
        
