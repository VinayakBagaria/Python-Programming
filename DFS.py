"""
5
3 2
3 1
1 4
1 5
"""

def dfs(graph,root):
    visited=[]
    stack=[root,]

    while(stack):

        node=stack.pop()

        if node not in visited:
            visited.append(node)

            stack.extend([x for x in graph[node] if x not in visited])

    return visited


n=int(input().strip())
graph = {}
start=0

for k in range(n-1):
    i,j=input().strip().split(' ')
    i,j=[int(i),int(j)]

    if(k==0):
        start=i

    graph.setdefault(i,[]).append(j)
    graph.setdefault(j, []).append(i)

print(graph)

print(dfs(graph,start))