import matplotlib.pyplot as plt
import numpy as nm
import segment
import path as path_module
import node

# Phase One:

class GraphClass():
    def __init__(self):
        self.nodes = []
        self.segments = []

def Graphfunc():
    test_graph = GraphClass()
    return test_graph

def addNode(graph, node):
    if node not in graph.nodes:
        graph.nodes.append(node)
        return True
    else:
        return False    

def addSegment(graph, name1, name2):
    node1 = None
    node2 = None
    for node in graph.nodes:
        if node.name == name1:
            node1 = node
        elif node.name == name2:
            node2 = node

    if node1 is not None and node2 is not None:
        graph.segments.append(segment.SegmentFunc(node1, node2))
        return True
    else:
        print("A segment cannot have two of the same nodes.")
        return False
 

def plot(g):
    plt.figure(figsize=(8, 6))
    for node in g.nodes:
        plt.plot(node.x, node.y, 'bo')
        plt.text(node.x, node.y, node.name)

    for segment in g.segments:
        node1 = segment.origin  
        node2 = segment.destination  
        plt.plot([node1.x, node2.x], [node1.y, node2.y], 'k-')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Graph Visualization')
    plt.grid(True)
    plt.show()

def plotNode(g, name):
    node_found = False
    for node in g.nodes:
        if node.name == name:
            node_found = True
            plt.figure(figsize=(8, 6))
            plt.plot(node.x, node.y, 'bo', markersize=10)
            plt.text(node.x, node.y, node.name, fontsize=12, ha='center', va='bottom')
            for neighbor_name in node.veins:
                neighbor = None
                for n in g.nodes:
                    if n.name == neighbor_name:
                        neighbor = n
                        break
                if neighbor:
                    plt.plot([node.x, neighbor.x], [node.y, neighbor.y], 'k-')
                    plt.text((node.x + neighbor.x) / 2, (node.y + neighbor.y) / 2, str(getSegmentCost(node, neighbor)), fontsize=10, ha='center', va='bottom')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title(f' Subgraph around node {name}')
            plt.grid(True)
            plt.show()
            break

    if not node_found:
        print(f"Node {name} not found.")

# Phase Two:

def findShortestPath(G, nameOrg, nameDst):
    # Initialize an empty list of paths
    paths = []
    
    # Initialize a path with the origin node
    origin_node = None
    for current_node in G.nodes:  # Renaming 'node' to 'current_node'
        if current_node.name == nameOrg:
            origin_node = current_node
            break
    
    if origin_node is None:
        return None  # Origin node doesn't exist
    
    # Create a new path object
    path_obj = path_module.Path()  # Assuming Path is defined somewhere
    path_obj.nodes_list.append(origin_node)
    paths.append(path_obj)
    
    while paths:
        # Search for the path with the lowest estimated cost
        min_path = min(paths, key=lambda p: p.total_cost)
        paths.remove(min_path)
        
        # Get the last node of the minimum path
        last_node = min_path.nodes_list[-1]
        
        # Check if the destination node is reached
        if last_node.name == nameDst:
            return min_path
        
        # Explore neighbors of the last node
        for neighbor in last_node.veins:
            # Check if the neighbor is already in the path to avoid cycles
            if neighbor in min_path.nodes_list:
                continue
            
            # Calculate the cost using the Distance function from node.py
            cost_to_neighbor = node.Distance(last_node, neighbor)  # Use 'current_node' instead of 'node'
            
            # Create a new path with the neighbor node
            new_path = path_module.Path()  # Assuming Path is defined somewhere
            new_path.nodes_list = min_path.nodes_list + [neighbor]
            new_path.costs_list = min_path.costs_list + [cost_to_neighbor]
            new_path.total_cost = min_path.total_cost + cost_to_neighbor
            
            # Add the new path to the list of paths
            paths.append(new_path)
    
    # If the loop ends and no path is fou



       
