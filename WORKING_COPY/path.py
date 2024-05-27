import matplotlib.pyplot as plt
import math

class Path:
    def __init__(self):
        self.nodes_list = []  # List of nodes in the path
        self.costs_list = []  # List of corresponding costs
        self.total_cost = 0   # Total cost of the path

def addNode(G, P, name):
    # Check if the node exists in the graph and is reachable from the last node in the path
    last_node = P.nodes_list[-1] if P.nodes_list else None
    node = G.getNode(name)
    if not node or (last_node and node not in G.getNeighbors(last_node)) or node in P.nodes_list:
        return False
    
    # Calculate the cost from the last node to the new node
    cost_to_node = G.getCost(last_node, node)
    
    # Add the node to the path and update the total cost
    P.nodes_list.append(node)
    P.costs_list.append(cost_to_node)
    P.total_cost += cost_to_node
    return True

def containsNode(P, name):
    return any(node.name == name for node in P.nodes_list)

def getCostToNode(P, name):
    for node, cost in zip(P.nodes_list, P.costs_list):
        if node.name == name:
            return cost
    return -1

def getApproxToDest(G, P, name):
    last_node = P.nodes_list[-1] if P.nodes_list else None
    dest_node = G.getNode(name)
    if not dest_node:
        return -1
    if last_node:
        return math.sqrt((last_node.x - dest_node.x)**2 + (last_node.y - dest_node.y)**2)
    return 0

def plotPath(G, P):    
    # Plot nodes
    for node in G.nodes:
        plt.plot(node.x, node.y, 'bo')
        plt.text(node.x, node.y, node.name)
    
    # Plot segments corresponding to the path
    for i in range(len(P.nodes_list) - 1):
        node1 = P.nodes_list[i]
        node2 = P.nodes_list[i + 1]
        plt.plot([node1.x, node2.x], [node1.y, node2.y], 'r-')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Graph with Minium Path(Total Cost: {})".format(P.total_cost))
    plt.grid(True)
    plt.show()

#New Function path.py PHASE 4

def pathToKML(path, nomFile):
    with open(nomFile, "r") as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        file.write('<Document>\n')

        # Add the path to the KML file
        for i in range(len(path)):
            file.write('<Placemark>\n')
            file.write('<name>' + str(i + 1) + '</name>\n')
            file.write('<description>' + 'Path' + '</description>\n')
            file.write('<LineString>\n')
            file.write('<coordinates>' + path[i] + '</coordinates>\n')
            file.write('</LineString>\n')
            file.write('</Placemark>\n')

        file.write('</Document>\n')
        file.write('</kml>\n')
