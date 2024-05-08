import matplotlib as plt
import numpy as nm

# Phase One:

class GraphClass():
    def __init__(self, nodes, segment):
        self.nodes = nodes
        self.segment = segment

def Graphfunc():
    test_graph = GraphClass("", "")
    return test_graph

def addNode(graph, node):
    i = 0
    poner = True
    while (i <= len[graph]):
        if(graph[i] == node):
            graph.nodes.append(node)
        i += 1
       

def addSegment(graph, name1, name2):

    # name1 might need to be node.names (?)

    i = 0
    nodo1_Encontrado = False
    nodo2_Encontrado = False
    while nodo1_Encontrado == False and nodo2_Encontrado == False:
        if graph.nodes[i] == name1:
            nodo1 = graph.nodes[i]
            nodo1_Encontrado == True

        elif graph.nodes[i] == name2:
            nodo2 = graph.nodes[i]
            nodo2_Encontrado == True

            i += 1

    if nodo1_Encontrado == True and nodo2_Encontrado == True:
        Segmendo = segment.SegmentFunc(nodo1, nodo2)
        return True

    else:
        print("A segment cannot have two of the same nodes.")
        return False
 



def plot(g):


def plotNode(g, name):


# Phase Two:

def FindShortestPath(G, nameOrg, nameDst):
       
