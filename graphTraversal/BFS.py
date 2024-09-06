from collections import deque

graph = {
    'a' : ['b', 'c'],
    'c' : ['e'],
    'b' : ['c', 'd'],
    'd' : ['e'],
    'e' : []
}


def bfs(graph, que, visited):

    while que:
        node = que.popleft()
        print(node)
        for nei in graph[node]:
            if nei not in visited and nei not in que:
                que.append(nei)

"""
Recursively
def bfs(graph, queue, visited=set()):
    if not queue:
        return
    
    node = queue.popleft()
    
    if node not in visited:
        print(node)
        visited.add(node)
        queue.extend(graph[node])
    
    bfs(graph, queue, visited)

"""

que = deque('a')
visited = set('a')
bfs(graph, que, visited)


