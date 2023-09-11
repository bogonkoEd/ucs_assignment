import heapq
import pydot
import io
from PIL import Image


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, start, end, cost):
        self.vertices[start].append((end, cost))
        self.vertices[end].append((start, cost))  # Assuming the graph is undirected

def ucs(graph, start, goal):
    queue = [(0, start)]  # Priority queue with (cost, node) tuples
    visited = set()
    ucs_tree = pydot.Dot(graph_type='graph')

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_node == goal:
            return current_cost, ucs_tree  # Return the cost and UCS tree when reaching the goal

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, edge_cost in graph.vertices[current_node]:
            if neighbor not in visited:
                heapq.heappush(queue, (current_cost + edge_cost, neighbor))
                edge = pydot.Edge(current_node, neighbor, label=str(edge_cost))
                ucs_tree.add_edge(edge)

    return None, ucs_tree  # If no path is found, return None and the UCS tree

def main():
    # Create a graph
    g = Graph()

    # Add vertices (nodes)
    g.add_vertex("SportsComplex")
    g.add_vertex("Siwaka")
    g.add_vertex("Ph.1A")
    g.add_vertex("Ph.1B")
    g.add_vertex("Phase2")
    g.add_vertex("STC")
    g.add_vertex("J1")
    g.add_vertex("Mada")
    g.add_vertex("Phase3")
    g.add_vertex("ParkingLot")

    # Add edges with associated costs
    g.add_edge("SportsComplex", "Siwaka", 450)
    g.add_edge("Siwaka", "Ph.1A", 10)
    g.add_edge("Ph.1A", "Ph.1B", 100)
    g.add_edge("Ph.1B", "Phase2", 112)
    g.add_edge("Phase2", "Phase3", 500)
    g.add_edge("Siwaka", "Ph.1B", 230)
    g.add_edge("Ph.1B", "STC", 50)
    g.add_edge("STC", "Phase2", 50)
    g.add_edge("STC", "ParkingLot", 250)
    g.add_edge("Ph.1A", "Mada", 850)
    g.add_edge("J1", "Mada", 200)
    g.add_edge("ParkingLot", "Mada", 200)

    # Find the optimal path cost from "SportsComplex" to "Phase3" and the UCS tree
    start_node = "Siwaka"
    goal_node = "Mada"
    result, ucs_tree = ucs(g, start_node, goal_node)

    if result is not None:
        print(f"Optimal path cost from {start_node} to {goal_node}: {result}")

        # Save the UCS tree as an image
        ucs_tree_file = 'ucs_tree.png'
        ucs_tree.write_png(ucs_tree_file)

        # Display the UCS tree image
        img = Image.open(ucs_tree_file)
        img.show()
    else:
        print(f"No path found from {start_node} to {goal_node}.")

if __name__ == "__main__":
    main()
