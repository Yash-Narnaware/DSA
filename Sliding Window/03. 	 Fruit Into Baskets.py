#Leetcode - https://leetcode.com/problems/fruit-into-baskets/description/

#keep expanding window till there are atmost 2 different types of fruits present in window when 3rd fruit appears shrink start till there are only two types of fruits.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        start, end = 0, 0
        present_fruits = {}

        res = 0

        while end < len(fruits):

            if fruits[end] not in present_fruits:
                if len(present_fruits) == 2:
                    res = max(res, end - start)

                    while len(present_fruits) == 2:
                        present_fruits[fruits[start]] -= 1
                        if present_fruits[fruits[start]] == 0:
                            del present_fruits[fruits[start]]
                        start += 1

                    end -= 1

                else:
                    present_fruits[fruits[end]] = 1
            else:
                present_fruits[fruits[end]] += 1

            end += 1

        res = max(res, end - start)

        return res
