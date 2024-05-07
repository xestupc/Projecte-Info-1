import matplotlib.pyplot as plt
import numpy as np
class Path:
   def __init__(self, nodes_list, costs_list, total_cost):
      self.nodes_list = nodes_list
      self.costs_list = costs_list
      self.total_cost = total_cost
    # must have
    # list of nodes of the path
    # list of corresponding costs
    # total cost of the path

def PathFunc(): # constructor 
    PathObject = Path ([], [], 0)
    return PathObject

def addNode(G, P, name):


def containsNode(P, name):


def getCostToNode(P, Name):



def getApproxToDest(G, P, name):


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
