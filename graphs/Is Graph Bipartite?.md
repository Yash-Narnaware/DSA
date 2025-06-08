# Is Graph Bipartite?

*Platform*: Leetcode | **Problem Number**: 785 | **Difficulty**: Medium  
*Category*: [Topic] | **Pattern**: [Pattern]  
*Priority*: Medium

## Problem Statement
[Original Problem Link]([URL](https://leetcode.com/problems/is-graph-bipartite/description/))  
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

- There are no self-edges (graph[u] does not contain u).
- There are no parallel edges (graph[u] does not contain duplicate values).
- If v is in graph[u], then u is in graph[v] (the graph is undirected).
- The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

## Approaches
- Veiw it as a map coloring problem with 2 colours
- Use visited array to store if node is colored or not. if coloured then what color it has. - use different numbers to represent different things e.g. 0 - unvisited, 1 - red, 2 - blue
- only visited unvisited neighbours of a node and pass the alternate colour for each neighbour
- if neighbour of node is already visited then check if it has same colour as current node if yes then return False

## Solution Code
```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:


        #0 - not visited, 1 - col1, 2 - col2
        visited = [0]*len(graph)

        def dfs(node,graph,visited,color):

            visited[node ] = color

            for neighbour in graph[node]:
                if visited[neighbour] == 0:
                    tmp1 = dfs(neighbour, graph, visited, 3-color)
                    if not tmp1:
                        return False

                else:
                    if color == visited[neighbour]:
                        return False

            return True

        # if graph have more than 1 component
        for i in range(len(graph)):
            if visited[i] == 0:
                q = dfs(i,graph,visited,1)
                if not q:
                    return False

        return True

        
```

## Edge Cases

## Notes
