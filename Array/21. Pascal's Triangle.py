#Leetcode - https://leetcode.com/problems/pascals-triangle/description/

#For generating each new row append 1 at begining and the use prev row elements to generate new row then add 1 at back of new row
#Also it can be solved using nCr.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]]

        for i in range(numRows-1):
            tmp = res[-1][:]
            j = len(tmp)

            tmp1 = [1]
            for k in range(1, j):
                tmp1.append(tmp[k-1] + tmp[k])
            tmp1.append(1)
            res.append(tmp1)
        return res
