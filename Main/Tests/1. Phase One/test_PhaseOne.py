
import matplotlib as plt
from _1_PhaseOne import graph
from _1_PhaseOne import node
from _1_PhaseOne import segment
from _2_PhaseTwo import path as path_module

# Main program for Phase 1
# Additionally, write a test program for the class Graph test_graph.py using as a base the program
# given below. Look at the function that generates the graph (crearGrafoEjemplo), it adds the nodes
# with their names and coordinates, then it adds the segments that connect the nodes. Extend to test
# the error conditions.

def crearGrafoEjemplo():
    G = graph.Graphfunc()
    graph.addNode(G, node.NodeClass("A", 1,  20,  []))
    graph.addNode(G, node.NodeClass("B", 8,  17,  []))
    graph.addNode(G, node.NodeClass("C", 15, 20,  []))
    graph.addNode(G, node.NodeClass("D", 18, 15,  []))
    graph.addNode(G, node.NodeClass("E", 2,  4 ,  []))
    graph.addNode(G, node.NodeClass("F", 6,  5 ,  []))
    graph.addNode(G, node.NodeClass("G", 12, 12,  []))
    graph.addNode(G, node.NodeClass("H", 10, 3,   []))
    graph.addNode(G, node.NodeClass("I", 19, 1,   []))
    graph.addNode(G, node.NodeClass("J", 13, 5,   []))
    graph.addNode(G, node.NodeClass("K", 3,  15,  []))
    graph.addNode(G, node.NodeClass("L", 4,  10,  []))

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

# Main - Phase One

Grph = crearGrafoEjemplo()
graph.plot(Grph)

# Get the minimum path
min_path = graph.findShortestPath(Grph, "A", "B")

# Plot the graph with the shortest path
# graph.plot(Grph)
path_module.plotPath(Grph, min_path)
# plt.show()

# plt.plot to paint the points
# plt.text to paint names and costs
# plt.arrow to paint the arrows of the segments
# plt.axis if we need to define the toal window displayed
# plt.grid to paint division lines
# plt.title to give it a title
# plt.show to show graph once built

