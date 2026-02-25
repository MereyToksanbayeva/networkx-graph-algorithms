import networkx as nx

# Create graph
G = nx.Graph()

# Add edges
G.add_edge("John", "Olivia", weight=7)
G.add_edge("Olivia", "Celine", weight=8)
G.add_edge("Chloe", "John", weight=7)
G.add_edge("Chloe", "Winston", weight=11)
G.add_edge("Celine", "Winston", weight=6)

# Remove Jack (as required)
# Jack and all edges connected to him disappear

print("=== Shortest Distances AFTER Removing Jack ===")

# Compute distances only for remaining nodes
for p1 in G.nodes():
    for p2 in G.nodes():
        if p1 != p2:
            try:
                dist = nx.dijkstra_path_length(G, p1, p2)
                print(f"{p1} -> {p2}: {dist}")
            except nx.NetworkXNoPath:
                print(f"{p1} -> {p2}: NO PATH")
