import networkx as nx

KG = nx.DiGraph()


KG.add_node("Apple", type="Fruit")
KG.add_node("Banana", type="Fruit")
KG.add_node("Cat", type="Animal")
KG.add_node("Dog", type="Animal")
KG.add_node("Denizli", type="City")
KG.add_node("Forest", type="Location")


KG.add_edge("Apple", "Denizli", relationship="grows_in")
KG.add_edge("Banana", "Forest", relationship="grows_in")
KG.add_edge("Cat", "Forest", relationship="lives_in")
KG.add_edge("Dog", "Forest", relationship="lives_in")
KG.add_edge("Apple", "Banana", relationship="similar_to")

def find_fruits_in_city(KG, city_name):
    result = []
    for u, v, data in KG.edges(data=True):
        if v == city_name and data.get("relationship") == "grows_in":
            if KG.nodes[u].get("type") == "Fruit":
                result.append(u)
    return result


def find_animals_in_location(KG, location):
    result = []
    for u, v, data in KG.edges(data=True):
        if v == location and data.get("relationship") == "lives_in":
            result.append(u)
    return result


def find_similar_items(KG, item):
    result = []
    for u, v, data in KG.edges(data=True):
        if u == item and data.get("relationship") == "similar_to":
            result.append(v)
    return result


print("Fruits growing in Denizli:", find_fruits_in_city(KG, "Denizli"))
print("Animals living in Forest:", find_animals_in_location(KG, "Forest"))
print("Items similar to Apple:", find_similar_items(KG, "Apple"))
