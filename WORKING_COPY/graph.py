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
        plt.text(node.x, node.y, node.name, size="x-large", weight="bold")

    for segment in g.segments:
        node1 = segment.origin  
        node2 = segment.destination  
        plt.arrow(node1.x, node1.y, node2.x - node1.x, node2.y - node1.y, 
            head_width=0.05, head_length=0.1, fc='c', ec='c')  # plot cyan arrows
        plt.text((node1.x + node2.x) / 2, (node1.y + node2.y) / 2, 
            f"{segment.cost:.3f}", size="x-small")  # plot segment costs

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Graph Visualization')
    plt.grid(True, linestyle="--", color="red")
    
    plt.show()

def plotNode(g, name):
    min_x= None
    max_x= None
    min_y= None
    max_y= None
    for i in g.nodes:
        if i.name==name:
            node=i

            plt.plot(i.x, i.y, color="purple", marker="p", markersize=10)
            plt.text(i.x, i.y, i.name, size="x-large")
        else:
            plt.plot(i.x, i.y, color="grey", marker="p", markersize=5)
            plt.text(i.x, i.y, i.name)

        if min_x == None or i.x < min_x:
            min_x = i.x

        if max_x == None or i.x > max_x:
            max_x = i.x

        if min_y == None or i.y < min_y:
            min_y = i.y

        if max_y == None or i.y > max_y:
            max_y = i.y


    for i in g.segments:
        if i.origin.name==name:
            plt.arrow(i.origin.x , i.origin.y, (i.destination.x - i.origin.x) , (i.destination.y - i.origin.y), color="grey")
            plt.text( (i.origin.x+((i.destination.x - i.origin.x)/2)), (i.origin.y+((i.destination.y - i.origin.y)/2)),  round(i.cost, 3))

    plt.axis([min_x,max_x,min_y, max_y])
    plt.grid()
    plt.title("Node and segments graph")
    plt.show()

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



       
