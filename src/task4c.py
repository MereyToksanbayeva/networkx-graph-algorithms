import networkx as nx

# Create the graph again
G = nx.Graph()
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

# Starting node (you can choose any)
start = "John"

# DFS traversal
dfs_order = list(nx.dfs_preorder_nodes(G, start))

# BFS traversal
bfs_order = list(nx.bfs_tree(G, start))

print("=== DFS Traversal starting from John ===")
print(dfs_order)

print("\n=== BFS Traversal starting from John ===")
print(bfs_order)
