
from _1_PhaseOne import node as node

""" ===========================================================================================
Program to test the node 
"""
Node1 = node.NodeClass("A", 200, 350, [])
Node2 = node.NodeClass("B", 400, 700, [])
Node3 = node.NodeClass("C", 500, 230, [])
Node4 = node.NodeClass("D", 600, 900, [])

node.addNeighbor(Node1, Node2)
node.addNeighbor(Node1, Node3)
node.addNeighbor(Node1, Node4)

node.printNodeChar(Node1)