#Leetcode - https://leetcode.com/problems/lfu-cache/description/


class Node:
    def __init__(self,key=None,value=0,next=None,prev=None, idx=0):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
        self.idx = idx
class LFUCache:

    def __init__(self, capacity: int):

        self.mapping = {}
        self.size = 0
        self.capacity = capacity
        self.adj_list = []
        for i in range(capacity):
            self.create_new_freq()

    def create_new_freq(self):
        t_head = Node()
        t_tail = Node()

        t_head.value = -1
        t_tail.value = -1

        t_head.next = t_tail
        t_tail.prev = t_head

        self.adj_list.append([t_head, t_tail])

    
    def get(self, key: int) -> int:

        if key in self.mapping:
            node = self.mapping[key]
            idx = node.idx

            #Remove node from that freq. DLL
            node.prev.next = node.next
            node.next.prev = node.prev

            #Add it in new freq DLL(inc freq by 1)
            if idx + 1 >= len(self.adj_list):
                self.create_new_freq()
                
            head = self.adj_list[idx+1][0]
            node.prev = head
            node.next = head.next
            head.next = node
            node.next.prev = node

            #Increase node idx(represents freq) by 1
            node.idx += 1

            return node.value

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value
            node.idx += 1

            #Remove node from that freq. DLL
            node.prev.next = node.next
            node.next.prev = node.prev

            #Add it in new freq DLL(inc freq by 1)
            if node.idx >= len(self.adj_list):
                self.create_new_freq()

            head = self.adj_list[node.idx][0]
            node.prev = head
            node.next = head.next
            head.next = node
            node.next.prev = node

        else:
            node = Node()
            node.key = key
            node.value = value
            node.idx = 0
            self.mapping[key] = node

            #Remove least frequent node if capacity is reached
            if self.size == self.capacity:
                for i in range(len(self.adj_list)):
                    tail = self.adj_list[i][1]
                    if tail.prev.value != -1:
                        break
                rm = tail.prev
                rm.prev.next = rm.next
                rm.next.prev = rm.prev

                del self.mapping[rm.key]
                self.size -= 1

            #Add new node
            head = self.adj_list[0][0]
            node.prev = head
            node.next = head.next
            head.next = node
            node.next.prev = node

            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



#Improved version - true O(1) operations - added var to keep track idx of to remove LFU node's list
class Node:
    def __init__(self,key=None,value=0,next=None,prev=None, idx=0):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
        self.idx = idx

class LFUCache:

    def __init__(self, capacity: int):

        self.mapping = {}
        self.size = 0
        self.capacity = capacity
        self.adj_list = []
        for i in range(capacity):
            self.create_new_freq()

        #var to store the index of list to remove least frequent node from
        self.rm_idx = 0

    def create_new_freq(self):
        t_head = Node()
        t_tail = Node()

        t_head.value = -1
        t_tail.value = -1

        t_head.next = t_tail
        t_tail.prev = t_head

        self.adj_list.append([t_head, t_tail])

    
    def get(self, key: int) -> int:

        if key in self.mapping:
            node = self.mapping[key]
            idx = node.idx

            #Remove node from that freq. DLL
            node.prev.next = node.next
            node.next.prev = node.prev

            #Add it in new freq DLL(inc freq by 1)
            if idx + 1 >= len(self.adj_list):
                self.create_new_freq()
                
            head = self.adj_list[idx+1][0]
            node.prev = head
            node.next = head.next
            head.next = node
            node.next.prev = node

            #Increase node idx(represents freq) by 1
            node.idx += 1

            #Update rm_index if required
            if self.rm_idx == idx and self.adj_list[idx][1].prev.value == -1:
                self.rm_idx += 1

            return node.value

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value
            node.idx += 1

            #Remove node from that freq. DLL
            node.prev.next = node.next
            node.next.prev = node.prev

            #Add it in new freq DLL(inc freq by 1)
            if node.idx >= len(self.adj_list):
                self.create_new_freq()

            head = self.adj_list[node.idx][0]
            node.prev = head
            node.next = head.next
            head.next = node
            node.next.prev = node

            #Check if rm_idx needs to be updated
            if self.rm_idx == node.idx - 1 and self.adj_list[self.rm_idx][1].prev.value == -1:
                self.rm_idx += 1

        else:
            node = Node()
            node.key = key
            node.value = value
            node.idx = 0
            self.mapping[key] = node

            #Remove least frequent node if capacity is reached
            if self.size == self.capacity:
                rm = self.adj_list[self.rm_idx][1].prev
                rm.prev.next = rm.next
                rm.next.prev = rm.prev

                del self.mapping[rm.key]
                self.size -= 1

            #Add new node
            head = self.adj_list[0][0]
            node.prev = head
            node.next = head.next
            head.next = node
            node.next.prev = node
            #Set rm_idx to be zero because we added new element and this new element now has the least freq.
            self.rm_idx = 0
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
