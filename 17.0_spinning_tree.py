class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices in the graph
        self.edges = []  # List of all edges in the form (weight, u, v)

    def add_edge(self, u, v, weight):
        """Add an edge to the graph."""
        self.edges.append((weight, u, v))

    def find(self, parent, vertex):
        """Find the parent of a vertex (with path compression)."""
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    def union(self, parent, rank, x, y):
        """Union of two sets based on rank."""
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        """Run Kruskal's algorithm to find the MST."""
        # Sort all edges in ascending order of weight
        self.edges.sort()
        mst = []  # List to store the MST
        parent = []  # Parent array for union-find
        rank = []  # Rank array for union-find

        # Initialize union-find structures
        for vertex in range(self.vertices):
            parent.append(vertex)
            rank.append(0)

        # Iterate through sorted edges and add to MST if no cycle is formed
        for weight, u, v in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:  # If adding this edge does not form a cycle
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst
# Create a graph with 6 vertices
g = Graph(6)

# Add edges (u, v, weight)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 9)
g.add_edge(3, 4, 5)
g.add_edge(3, 5, 7)
g.add_edge(4, 5, 11)

# Get the Minimum Spanning Tree
mst = g.kruskal_mst()

# Print the MST and its total cost
print("Edges in the Minimum Spanning Tree:")
total_cost = 0
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
    total_cost += weight
print(f"Total cost of the Minimum Spanning Tree: {total_cost}")
