import node
import segment
import graph
import path as path_module
import matplotlib.pyplot as plt
""" ===========================================================================================
Program to test the graph
"""
def crearGrafoEjemplo ():
    G = graph.Graphfunc()
    graph.addNode(G, node.NodeClass("A", 1,  20,  ))
    graph.addNode(G, node.NodeClass("B", 8,  17,  ))
    graph.addNode(G, node.NodeClass("C", 15, 20,  ))
    graph.addNode(G, node.NodeClass("D", 18, 15,  ))
    graph.addNode(G, node.NodeClass("E", 2,  4 ,  ))
    graph.addNode(G, node.NodeClass("F", 6,  5 ,  ))
    graph.addNode(G, node.NodeClass("G", 12, 12,  ))
    graph.addNode(G, node.NodeClass("H", 10, 3,   ))
    graph.addNode(G, node.NodeClass("I", 19, 1,   ))
    graph.addNode(G, node.NodeClass("J", 13, 5,   ))
    graph.addNode(G, node.NodeClass("K", 3,  15,  ))
    graph.addNode(G, node.NodeClass("L", 4,  10,  ))

    graph.addSegment(G, "A","B")
    graph.addSegment(G, "A","E")
    graph.addSegment(G, "A","K")
    graph.addSegment(G, "B","A")
    graph.addSegment(G, "B","C")
    graph.addSegment(G, "B","F")
    graph.addSegment(G, "B","K")
    graph.addSegment(G, "B","G")
    graph.addSegment(G, "C","D")
    graph.addSegment(G, "C","G")
    graph.addSegment(G, "D","G")
    graph.addSegment(G, "D","H")
    graph.addSegment(G, "D","I")
    graph.addSegment(G, "E","F")
    graph.addSegment(G, "F","L")
    graph.addSegment(G, "G","B")
    graph.addSegment(G, "G","F")
    graph.addSegment(G, "G","H")
    graph.addSegment(G, "I","D")
    graph.addSegment(G, "I","J")
    graph.addSegment(G, "J","I")
    graph.addSegment(G, "K","A")
    graph.addSegment(G, "K","L")
    graph.addSegment(G, "L","K")
    graph.addSegment(G, "L","F")
   
    return G

#Main
print ("Probando el grafo...")
G = crearGrafoEjemplo()
graph.plot(G)
graph.plotNode(G, "C")
print ("OK")

min_path = graph.findShortestPath(G, "A", "B")

# Plot the graph with the shortest path
# graph.plot(Grph)
path_module.plotPath(G, min_path)