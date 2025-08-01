#Leetcode - https://leetcode.com/problems/remove-k-digits/

#remember edge cases - if we traverse whole string and k is non zero then remove last k digits. remove leading zeros from answer
#We want to remove digits from left side which are big than their right side digits.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if k == len(num):
            return '0'
        stack = []

        for j, i in enumerate(num):
            #keep removing if stack element is > current element(means better option is available)
            while stack and int(stack[-1]) > int(i) and k > 0:
                k -= 1
                stack.pop()

            #Removed K digits
            if k == 0:
                if stack:
                    tmp = str(int("".join(stack)))
                    return tmp + num[j:]
                else:
                    return str(int(num[j:]))
            
            stack.append(i)

        #Traversed num but still we can remove some digits - remove from back
        while k:
            stack.pop()
            k -= 1

        #Remove leading zeros
        i = 0
        n = len(stack)
        while i < n and stack[i] == '0':
            i += 1
        
        return "".join(stack[i:]) if i < n else '0'
        
