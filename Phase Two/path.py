import matplotlib.pyplot as plt
import numpy as np
class Path:
    # must have
    # list of nodes of the path
    # list of corresponding costs
    # total cost of the path

def PathFunc():
    # constructor 


def addNode(G, P, name):


def containsNode(P, name):


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
