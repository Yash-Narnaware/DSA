# Traversal Techniques(BFS and DFS)

*Platform*: TUF | **Problem Number**: [Number] | **Difficulty**: Easy
*Category*: Graph Traversal | **Pattern**: [Pattern]  
*Priority*: [High/Medium/Low/None] (e.g., High for extra study)

## Problem Statement
[Original Problem Link](https://takeuforward.org/plus/dsa/problems/traversal-techniques)  
Given an undirected connected graph with V vertices numbered from 0 to V-1, the task is to implement both Depth First Search (DFS) and Breadth First Search (BFS) traversals starting from the 0th vertex. The graph is represented using an adjacency list where adj[i] contains a list of vertices connected to vertex i. Visit nodes in the order they appear in the adjacency list.

## Approaches

### 1. Breadth First Search(BFS)
- Initialize the queue with source node inside it.
- While queue is not empty keep popping start of the queue and add the unvisited neighbours of that popped node to queue.

### 2. Depth First Search
- Define a function dfs
- Recursively visit the neighbour of node

## Solution Code
``` python
class Solution:
    def dfsOfGraph(self, V, adj):

      visited = set()
      def dfs(node,visited):
        visited.add(node)
        res.append(node)
        for n in adj[node]:
          if n not in visited:
            dfs(n,visited)
      res = []
      dfs(0,visited)
      return res
        
    
    def bfsOfGraph(self, V, adj):
      res = []
      queue = deque([0])
      visited = set([0])

      while queue:
        cur = queue.popleft()
        res.append(cur)
        
        for n in adj[cur]:
          if n not in visited:
            visited.add(n)
            queue.append(n)

      return res
```

## Edge Cases

## Notes
