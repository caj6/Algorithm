class Graph:
    def __init__(self, adj_list):
        self.graph = adj_list  # Adjacency list representation of graph

    def remove_edge(self, u, v):
        # Remove the edge from u to v and from v to u (since the graph is undirected)
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def is_valid_next_edge(self, u, v):
        # Check if the edge u-v is valid to be part of the Eulerian path or circuit
        if len(self.graph[u]) == 1:
            return True  # If u has only one adjacent vertex, return True

        # Otherwise, we do a DFS to count reachable vertices from u
        visited = {key: False for key in self.graph}
        count_before_removal = self.dfs(u, visited)

        # Remove the edge and check how many vertices are reachable after removal
        self.remove_edge(u, v)
        visited = {key: False for key in self.graph}
        count_after_removal = self.dfs(u, visited)

        # Add the edge back
        self.graph[u].append(v)
        self.graph[v].append(u)

        # If the number of reachable vertices decreases after the removal,
        # the edge u-v is a bridge and should not be used
        return count_before_removal == count_after_removal

    def dfs(self, v, visited):
        visited[v] = True
        count = 1
        for adj in self.graph[v]:
            if not visited[adj]:
                count += self.dfs(adj, visited)
        return count

    def fleury(self, start_vertex):
        circuit = []  # To store the Eulerian path or circuit
        current_vertex = start_vertex

        while len(self.graph[current_vertex]) > 0:
            # Iterate over all adjacent vertices of the current vertex
            for next_vertex in self.graph[current_vertex]:
                # Check if this edge can be safely removed
                if self.is_valid_next_edge(current_vertex, next_vertex):
                    circuit.append(current_vertex)  # Add the current vertex to the circuit
                    self.remove_edge(current_vertex, next_vertex)  # Remove the edge
                    current_vertex = next_vertex  # Move to the next vertex
                    break

        circuit.append(current_vertex)  # Append the last vertex
        return circuit


# Example Usage:
adj_list = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

graph = Graph(adj_list)
eulerian_circuit = graph.dfs()
print("Eulerian Circuit/Path:", eulerian_circuit)
