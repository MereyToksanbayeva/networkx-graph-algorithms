import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Edges from the given figure (with weights)
G.add_edge("John", "Olivia", weight=7)
G.add_edge("John", "Jack", weight=9)
G.add_edge("John", "Chloe", weight=7)

G.add_edge("Olivia", "Jack", weight=4)
G.add_edge("Olivia", "Celine", weight=8)

G.add_edge("Jack", "Celine", weight=5)
G.add_edge("Jack", "Winston", weight=7)

G.add_edge("Celine", "Winston", weight=6)

G.add_edge("Chloe", "Jack", weight=5)
G.add_edge("Chloe", "Winston", weight=11)

# Drawing
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1800, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Social Network Graph")
plt.show()
