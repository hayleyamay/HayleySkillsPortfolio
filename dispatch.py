import osmnx as ox

place_name = "Chinatown, San Francisco, California, USA"
graph = ox.graph_from_place(place_name, network_type="drive")

print(graph)
print(f"Nodes: {len(graph.nodes)}")
print(f"Edges: {len(graph.edges)}")