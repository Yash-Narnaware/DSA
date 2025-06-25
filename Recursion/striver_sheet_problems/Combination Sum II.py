#Leetcode - https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        mp = [0]*50
        for i in candidates:
            mp[i-1] += 1

        def comb(cur_set,mp,cur_sum,res):

            if cur_sum == target:
                res.add(tuple(sorted(cur_set)))
                return 

            if cur_sum > target:
                return 
            
            for i in range(50):
                if mp[i] != 0:
                    if cur_sum + i+1 > target:
                        break
                    cur_set.append(i+1)
                    mp[i] -= 1
                    comb(cur_set,mp,cur_sum+i+1,res)

                    mp[i] += 1
                    cur_set.pop()

        res = set()
        comb([],mp,0,res)

        return list(res)

        


        
