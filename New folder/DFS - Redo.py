def dfs(graph,root):
    visited=[]

    # current node under consideration from where we start; empty at last
    stack=[root,]

    while(stack):
        node=stack.pop()

        if node not in visited:
            # mark node as visited
            visited.append(node)
            # mark the node's children in stack if it is not visited as yet. If not visited the child, we didn't visit its children.
            stack.extend([x for x in graph[node] if x not in visited])

    return visited


vertex_count=int(input())
graph={}

start=0

for k in range(vertex_count-1):
    i,j=input().split(' ')
    i,j=[int(i),int(j)]

    if k==0:
        start=i


    graph.setdefault(i,[]).append(j)
    graph.setdefault(j, []).append(i)


print(dfs(graph,start))
print(graph)