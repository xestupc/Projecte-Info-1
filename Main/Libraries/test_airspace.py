import AirSpaceLib
import GraphLib

""" ===========================================================================================
Program to test the airspace classes
"""
A = AirSpaceLib.buildAirSpace("Cat")
G = AirSpaceLib.buildAirGraph(A)
GraphLib.plot(G)
GraphLib.plotNode(G,"GODOX")
c = GraphLib.findShortestPath(G,"LEBL","LEZG")
GraphLib.plotPath(G,c)