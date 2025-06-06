# [Connected Components]

*Platform*: [TUF] | **Problem Number**: [Number] | **Difficulty**: [Easy]  
*Category*: BFS/DFS traversal | **Pattern**: [Pattern]  
*Priority*: [Low]

## Problem Statement
[Original Problem Link](https://takeuforward.org/plus/dsa/problems/connected-components)  
Given a undirected Graph consisting of V vertices numbered from 0 to V-1 and E edges. The ith edge is represented by [ai,bi], denoting a edge between vertex ai and bi. We say two vertices u and v belong to a same component if there is a path from u to v or v to u. Find the number of connected components in the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

## Approaches
- Use visited set to keep track of all the visited nodes.
- Iterate through all the nodes and if node is unvisited initiate BFS/DFS traversal from it.
- The number of times we initiate this call to traversal function is the number of componenets present in the graph.

## Solution Code
```python
class Solution:
    def findNumberOfComponent(self, E, V, edges):

        graph = [[] for _ in range(V)]

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        
        def dfs(node,visited):

            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    dfs(n,visited)

        res = 0
        visited = set()
        for i in range(V):
            if i not in visited:
                res += 1
                dfs(i,visited)

        return res
```

## Edge Cases

## Notes
