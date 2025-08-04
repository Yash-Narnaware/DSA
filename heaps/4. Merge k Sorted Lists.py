#Leetcode - https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_hp = []
        for i in range(len(lists)):
            if lists[i]:
                min_hp.append((lists[i].val, i, lists[i].next))

        heapq.heapify(min_hp)

        dummy = ListNode()
        head = dummy

        while min_hp:
            elem = heapq.heappop(min_hp)
            dummy.next = ListNode(elem[0])
            dummy = dummy.next

            if elem[2]:
                heapq.heappush(min_hp,(elem[2].val, elem[1], elem[2].next))

        return head.next

        
