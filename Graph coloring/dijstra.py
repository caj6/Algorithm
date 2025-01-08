import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def min_distance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        parent = [-1] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)
        self.draw_shortest_path(src, parent)
        
    def draw_shortest_path(self, src, parent):
        G = nx.Graph()
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != 0:
                    G.add_edge(i, j, weight=self.graph[i][j])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        # Draw the graph
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', linewidths=1, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        # Highlight the shortest path tree
        edges = []
        for i in range(self.V):
            if parent[i] != -1:
                edges.append((parent[i], i))

        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)

        plt.show()
        
    def draw_graph(self):
        G = nx.Graph()
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != 0:
                    G.add_edge(i, j, weight=self.graph[i][j])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', linewidths=1, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        
# Example usage:
if __name__ == "__main__":
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    g.draw_graph()
    g.dijkstra(0)