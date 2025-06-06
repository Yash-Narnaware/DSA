from collections import defaultdict

n = int(input())

if n == 2:
    print(0)
    exit()

if n % 2 == 1:
    print(-1)
    exit()

edges = []
adj = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))
    adj[u].append(v)
    adj[v].append(u)



tmp = {}
def dfs(node,parent):

    tmp1 = 0
    for nei in adj[node]:
        if nei != parent:
            tmp1 += dfs(nei,node)

    tmp[node] = 1 + tmp1
    return tmp[node]

dfs(1,-1)

res = 0
for i,j in edges:
    if tmp[i] > tmp[j]:
        parent = i
        child = j
    else:
        parent = j
        child = i

    if tmp[child] % 2 == 0:
        res += 1
print(res)

    
