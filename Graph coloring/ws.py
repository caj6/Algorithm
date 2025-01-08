#backtrack algo
def is_safe(graph, v, color, c):
    for i in graph[v]:
        if color[i] == c:
            return False
    return True

def graph_coloring(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, v, color, c):
            color[v] = c
            if graph_coloring(graph, m, color, v + 1):
                return True
            color[v] = 0

    return False

def solve_graph_coloring(graph, m):
    color = [0] * len(graph)
    if graph_coloring(graph, m, color, 0):
        return color
    else:
        return "No solution"

#-----------------------------------------------------------------------------------------------------------
#algo
def dsatur(graph):
    n = len(graph)
    colors = [-1] * n
    saturation = [0] * n
    degree = [len(graph[i]) for i in range(n)]
    
    colors[degree.index(max(degree))] = 0  # Assign first color to the highest degree vertex

    for _ in range(n - 1):
        # Select the vertex with the highest saturation and then highest degree
        max_saturation = max(saturation)
        candidates = [i for i in range(n) if colors[i] == -1 and saturation[i] == max_saturation]
        vertex = max(candidates, key=lambda x: degree[x])

        # Assign the smallest available color to the chosen vertex
        available = [True] * n
        for neighbor in graph[vertex]:
            if colors[neighbor] != -1:
                available[colors[neighbor]] = False

        color = available.index(True)
        colors[vertex] = color

        # Update saturation of the neighbors
        for neighbor in graph[vertex]:
            if colors[neighbor] == -1:
                saturation[neighbor] += 1

    return colors

#-------------------------------------------------------------------------------------------------------------
#algo
def welsh_powell(graph):
    vertices = len(graph)
    degree_sequence = sorted(range(vertices), key=lambda x: len(graph[x]), reverse=True)

    result = [-1] * vertices
    available = [False] * vertices

    for u in degree_sequence:
        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = True

        cr = 0
        while cr < vertices and available[cr]:
            cr += 1

        result[u] = cr
        available = [False] * vertices

    return result

#------------------------------------------------------------------------------------------------------
#algo
def gluttony(graph):
    n = len(graph)
    result = [-1] * n  # Store colors of vertices
    result[0] = 0      # Assign the first color to the first vertex

    available = [False] * n  # Tracks available colors for each vertex

    # Assign colors to remaining vertices
    for u in range(1, n):
        # Mark colors used by adjacent vertices
        for i in graph[u]:
            if result[i] != -1:
                available[result[i]] = True

        # Find the first available color
        cr = 0
        while cr < n and available[cr]:
            cr += 1

        result[u] = cr  # Assign the found color

        # Reset available colors for next vertex
        available = [False] * n

    return result

#----------------------------------------------------------------------------------------------------------
#algo
def fleury(g):
    circuit = [];
    vertex = [0];

#--------------------------------------------------------------------------------------------------------
#path
def pathy(graph, start, end, path=[]):
    path = path + [start];
    if start == end:
        return path;
    if start not in graph:
        return None;
    for node in graph[start]:
        if node not in path:
            newpath = pathy(graph, node, end, path);
            if newpath:
                return newpath;
    return None;

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')  

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']};
start = 'A';
end = 'D';
path = pathy(graph, start, end)
print("DFS starting from node", start)
dfs(graph, start)
#if path:
    #print(f"Path from {start} to {end}: {path}")
#else:
    #print(f"No path found from {start} to {end}")

#---------------------------------------------------------------------------------------------------------------------------
# shortest path
def shortest_path(graph, start, end, path=[]):
    path = path + [start];
    if start == end:
        return path;
    if start not in graph:
        return None;
    shortest = None;
    for node in graph[start]:
        if node not in path:
            newpath = shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def find_shortest_path(graph, start, end):
        dist = {start: [start]}
        q = deque(start)
        while len(q):
            at = q.popleft()
            for next in graph[at]:
                if next not in dist:
                    dist[next] = [dist[at], next]
                    q.append(next)
        return dist.get(end)

#-----------------------------------------------------------------------------------------------------------------------------
#all path
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return [];
    paths = [];
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths