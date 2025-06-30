#Leetcode - https://leetcode.com/problems/longest-common-prefix/description/


#@ approaches i applied - 1.find min lenght of words and then for index 0 till min lenght check chars of all words for that idx if not same then return prefix string formed till now if same for all words then add that char to prefix string.
#2. defined a function to calculate maximum prefix and pass result of previous words to calculate max prefix will next words and so on

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_lenght = 201
        fin_str = ""

        if len(strs) == 1: 
            return strs[0]

        if len(strs) == 0:
            return fin_str

        for i in strs:
            if len(i) < min_lenght:
                min_lenght = len(i)
            
        for i in range(min_lenght):
            for j in range(len(strs)-1):
                if strs[j][i] == strs[j+1][i]:
                    continue
                else:
                    return fin_str
            fin_str = fin_str + strs[0][i]
        return fin_str

        
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def cal_pref(a,b):

            n1 = len(a)
            n2 = len(b)
            res = ''
            i = 0

            while i < min(n1, n2):
                if a[i] != b[i]:
                    break
                res += a[i]
                i += 1
            return res

        n = len(strs)
        if n == 1:
            return strs[0]

        res = strs[0]
        for i in range(1, n):
            res = cal_pref(res, strs[i])
            if res == '':
                return ''

        return res
