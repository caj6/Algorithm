import pandas as pd
import networkx as nx
from typing import List
from collections import defaultdict
import heapq
import math
from pathlib import Path

class g:
    def __init__(self):
        self.graph = defaultdict(list);
        self.nodes = set();
        self.task_info = {};
        self.svg_width = 800;
        self.svg_height = 600;
        self.padding = 50;
        
    def read_csv_file(self, file_path):
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")
        
        # Clear any existing data
        self.graph.clear()
        self.nodes.clear()
        self.task_info.clear()
        
        with open(file_path, 'r') as file:
            # Read first line to check format
            first_line = file.readline().strip()
            # Reset file pointer
            file.seek(0)
            
            # Determine if file has headers
            if 'Task' in first_line:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        task_id = self.parse_task_id(row['Task'])
                        start = int(row['Start'])
                        end = int(row['End'])
                        
                        # Store task information
                        self.task_info[task_id] = {
                            'start': start,
                            'end': end,
                            'original_id': row['Task']  # Store original ID for display
                        }
                        
                        # Add nodes to our set
                        self.nodes.add(start)
                        self.nodes.add(end)
                        
                        # Weight is the time difference
                        weight = end - start
                        
                        # Add edges in both directions
                        self.graph[start].append((end, weight))
                        self.graph[end].append((start, weight))
                        
                    except ValueError as e:
                        print(f"Warning: Skipping invalid row: {row}")
                        continue
                
        print(f"Processed file {file_path.name}")
        print(f"Found {len(self.task_info)} tasks")
        print(f"Time points: {sorted(self.nodes)}")

    def adjacencylist(adj, self.task):
        for i in range (0, V):
            print(i, " " ,end="")
            for x in  adj[i]: 
                print(x," ",end="")
            print()
            
    def draw():
        G = nx.Graph();
        for index, row in data.iterrows():
            G.add_edge(row['start'], row['end'], weight=1);
        print(G.edges(data=True));

        pos = nx.spring_layout(G);
        labels = nx.get_edge_attributes(G, 'weight');
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', linewidths=1, font_size=10);
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels);
        plt.show();
        
    def colour_vertices(graph):
        vertices = sorted((list(graph.keys())));
        colour_graph = {};

        for vertex in vertices:
            unused_colours = len(vertices) * [True];

            for neighbor in graph[vertex]:
                if neighbor in colour_graph:
                    colour = colour_graph[neighbor];
                    unused_colours[colour] = False;
            for colour, unused in enumerate(unused_colours):
                if unused:
                    colour_graph[vertex] = colour;
                    break;
        return colour_graph;
    
    def main():
        try:
            visualizer = g();
            file_path = Path(r"C:\Users\junio\OneDrive\Documents\CESI\A3\Algo\Algo6\task_intervals_instances\task_intervals_1.csv")
            visualizer.read_csv_file(file_path);
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
