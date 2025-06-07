# Number of Provinces

*Platform*: Leetcode | **Problem Number**: 547 | **Difficulty**: Medium  
*Category*: [Topic] | **Pattern**: [Pattern]  
*Priority*: Low

## Problem Statement
[Original Problem Link](https://leetcode.com/problems/number-of-provinces/description/)  
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

## Approaches

- Same as calculating the number of components of the graph.

## Solution Code
```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        adj = [[] for _ in range(len(isConnected))]

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    adj[i].append(j)

        def dfs(node,visited):

            visited.add(node)

            for n in adj[node]:
                if n not in visited:
                    dfs(n,visited)

        res = 0
        visited = set()
        for i in range(len(isConnected)):
            if i not in visited:
                res += 1
                dfs(i,visited)
        return res
        
```

## Edge Cases

## Notes
