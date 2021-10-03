# Depth First Search using Python

graph = {
  '6': ['1', '8'],
  '1': ['5'],
  '8': ['10'],
  '5': ['3'],
  '3': [],
  '10': []
}
visited = set()

def DFS(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)

print("Depth First Search for the given Graph:")
DFS(visited, graph, '6')