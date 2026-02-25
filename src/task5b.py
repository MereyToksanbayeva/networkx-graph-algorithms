import networkx as nx

# Create a directed knowledge graph
KG = nx.DiGraph()

# Add nodes (entities)
KG.add_node("Apple", type="Fruit")
KG.add_node("Banana", type="Fruit")
KG.add_node("Cat", type="Animal")
KG.add_node("Dog", type="Animal")
KG.add_node("Denizli", type="City")
KG.add_node("Forest", type="Location")

# Add relationships
KG.add_edge("Apple", "Denizli", relationship="grows_in")
KG.add_edge("Banana", "Forest", relationship="grows_in")
KG.add_edge("Cat", "Forest", relationship="lives_in")
KG.add_edge("Dog", "Forest", relationship="lives_in")
KG.add_edge("Apple", "Banana", relationship="similar_to")

# Print graph info
print("Nodes:", KG.nodes(data=True))
print("Edges:", KG.edges(data=True))
