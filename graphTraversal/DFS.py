graph = {
    'a' : ['b', 'c'],
    'c' : ['e'],
    'b' : ['c', 'd'],
    'd' : ['e'],
    'e' : []
}


def dfs(graph, stack, visited):

    while stack:
        node = stack.pop()
        print(node)
        visited.add(node)
        for nei in graph[node]:
            if nei not in visited:
                stack.append(nei)



"""
Recursively
def dfs(graph, source, visited):
    if not source:
        return 
    
    print(source)
    visited.add(source)
    for nei in graph[source]:
        if nei not in visited:
            dfs(graph, nei, visited)
"""


visited = set()
stack = ['a']
dfs(graph, stack, visited)
