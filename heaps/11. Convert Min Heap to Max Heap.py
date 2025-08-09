#GFG - https://www.geeksforgeeks.org/problems/convert-min-heap-to-max-heap-1666385109/1

#Heapify the array. 
#they have given min heap in form of level order traversal and heaps are basically binary trees so we can heapify from last non leaft node till root. see it as filling each internal node place with correct node.

#My inital approach - not so clean - remember if left == right and parent is not largest then we have to swap with left child.

class Solution:
    def convertMinToMaxHeap(self, N, arr):

        for i in range((N // 2) - 1, -1, -1):
            cur = i
            
            while cur < N // 2:

                if 2 * cur + 1 >= N:
                    left = float('-inf')
                else:
                    left = arr[2 * cur + 1]
                    
                if 2 * cur + 2 >= N:
                    right = float('-inf')
                else:
                    right = arr[2 * cur + 2]
                    
                if arr[cur] > left and arr[cur] > right:
                    break
                
                if left < right:
                    arr[cur], arr[2 * cur + 2] = arr[2 * cur + 2], arr[cur]
                    cur = 2 * cur + 2
                    
                else:
                    arr[cur], arr[2 * cur + 1] = arr[2 * cur + 1], arr[cur]
                    cur = 2 * cur + 1
                    



#Better Approach - more clean way to do it.

class Solution:
    def convertMinToMaxHeap(self, N, arr):

        for i in range((N // 2) - 1, -1, -1):
            
            largest = i
            cur = i
            
            while True:
                left = 2 * cur + 1
                right = 2 * cur + 2
                
                
                if left < N and arr[left] > arr[largest]:
                    largest = left
                
                if right < N and arr[right] > arr[largest]:
                    largest = right
                    
                if largest == cur:
                    break
                
                arr[largest], arr[cur] = arr[cur], arr[largest]
                cur = largest

            
                    
