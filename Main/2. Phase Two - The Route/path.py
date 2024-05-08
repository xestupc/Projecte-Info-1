
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

    xpoints= np.array([])
    ypoints= np.array([])

    
    for node in G.nodes:
    
        xpoints.append(G.nodes[node.xcord])
        ypoints.append(G.nodes[node.ycord])

    plt.plot(xpoints, ypoints)

    plt.scatter(xpoints, ypoints, color='red', marker='*')
    plt.show()

    # falta pintar el path len entre points
