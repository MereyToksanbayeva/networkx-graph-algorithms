import networkx as nx

# Create graph
G = nx.Graph()

# Add weighted edges exactly as in the figure
G.add_edge("John", "Olivia", weight=7)
G.add_edge("Olivia", "Celine", weight=8)
G.add_edge("Olivia", "Jack", weight=4)
G.add_edge("John", "Jack", weight=9)
G.add_edge("John", "Chloe", weight=7)
G.add_edge("Chloe", "Jack", weight=5)
G.add_edge("Chloe", "Winston", weight=11)
G.add_edge("Jack", "Celine", weight=5)
G.add_edge("Celine", "Winston", weight=6)
G.add_edge("Jack", "Winston", weight=7)

# Print all shortest distances
print("=== Shortest Distances Between All Pairs ===")
for person1 in G.nodes():
    for person2 in G.nodes():
        if person1 != person2:
            dist = nx.dijkstra_path_length(G, person1, person2)
            print(f"{person1} -> {person2}: {dist}")
