#Leetcode - https://leetcode.com/problems/merge-sorted-array/description/

#Start merging from behind and have to handle cases like when pointer in nums  < 0 or pointer in num1 < 0.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        end_nums1 = m-1
        end_nums2 = n-1
        
        insert_pos = len(nums1) - 1

        while end_nums2 >=0:

            if end_nums1 < 0:
                nums1[insert_pos] = nums2[end_nums2]
                end_nums2 -= 1
                insert_pos -= 1
                continue

            if nums2[end_nums2] >= nums1[end_nums1]:
                nums1[insert_pos] = nums2[end_nums2]
                
                insert_pos -= 1
                end_nums2 -= 1
            else:
                nums1[insert_pos] = nums1[end_nums1]

                insert_pos -= 1
                end_nums1 -= 1


        
