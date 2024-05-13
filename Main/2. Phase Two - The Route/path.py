import matplotlib.pyplot as plt

class Path:
    def __init__(self, nodes_list, costs_list, total_cost):
        self.nodes_list = nodes_list
        self.costs_lists = costs_list
        self.total_cost = total_cost
    # must have
    # list of nodes of the path
    # list of corresponding costs
    # total cost of the path

def PathFunc(): # constructor 
    PathObject = Path([], [], 0)
    return PathObject
    

def addNode(G, P, name):
    # Graph Path Str --> Bool
    


    return True

    return False

def containsNode(P, name):


def getCostToNode(P, Name):


def getApproxToDest(G, P, name):
    # Graph, Path and String --> Number
    # Calculates best approximation between last node in paht and parameter node.
    # The node does not need to be reachable from the path.
    # Returns distance(last_node_path, parameter_node)


def plotPath(G, P):

    

def plotPath(G, P):
#Initialize lists to store node coordinates
    xpoints= []
    ypoints= []

    #get coordinates of nodes in path P
    for node in P:
    
        xpoints.append(G.nodes[node.xcord])
        ypoints.append(G.nodes[node.ycord])

    #plot the path P
    plt.plot(xpoints, ypoints)

 #highlight nodes in path
    plt.scatter(xpoints, ypoints, color='red', marker='*')

#add title and axis to the plot
    plt.title("Graph Path")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)
    
    #to show path len betwwen nodes
    total_length = 0
    for i in range(len(P) - 1):
        start_node = P[i]
        end_node = P[i + 1]
        edge_length = G.edges[start_node, end_node]['weight']  # Assuming edge weight represents length
        total_length += edge_length
        #to show path length betwween nodes right in the middle of the segment
        plt.text((xpoints[i] + xpoints[i + 1]) / 2, (ypoints[i] + ypoints[i + 1]) / 2, f"{edge_length:.2f}", ha='center', va='center')

    #show total length of path
    plt.text(0.5, -0.1, f"Total Path Length: {total_length:.2f}", ha='center', va='center', transform=plt.gca().transAxes)

    
    #to ahow plot
    plt.show()


