import AirSpace
import graph
""" ===========================================================================================
Program to test the airspace classes
"""
A = AirSpace.buildAirSpace("Cat")
G = AirSpace.buildAirGraph(A)
graph.plot(G)
graph.plotNode(G,"GODOX")
c = graph.findShortestPath(G,"LEBL","LEZG")
graph.plotPath(G,c)