#Leetcode - https://leetcode.com/problems/hand-of-straights/description/


#My approach - 
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)

        if n % groupSize != 0:
            return False

        freq = Counter(hand)

        min_hp = []

        for elem, freq in freq.items():
            min_hp.append((elem, freq))
        
        heapq.heapify(min_hp)

        while min_hp:

            tmp = []
            for i in range(groupSize):
                if min_hp:
                    elem, freq = heapq.heappop(min_hp)
                else:
                    return False
                if tmp:
                    if elem != tmp[-1][0] + 1:
                        return False
                freq -= 1
                tmp.append((elem, freq))
                
            for elem, freq in tmp:
                if freq > 0:
                    heapq.heappush(min_hp, (elem, freq))

        return True



#Approach 2: use the hashmap to check if next element is present or not

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)

        if n % groupSize != 0:
            return False

        freq = Counter(hand)

        min_hp = []

        for elem, f in freq.items():
            min_hp.append(elem)
        
        heapq.heapify(min_hp)

        while min_hp:
            st = min_hp[0]
            for i in range(st, st + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1

                #only top of the heap is allowed to have freq zero then later elements can have freq 0.
                if freq[i] == 0:
                    if i != min_hp[0]:
                        return False
                    heapq.heappop(min_hp)

        return True

        
