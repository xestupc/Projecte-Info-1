from Libraries import AirSpaceLib, Flightplan, GraphLib, NavAirportLib, NavPointLib, NavSegmentLib, NodeLib, PathLib, SegmentLib,WaypointLib

<<<<<<< HEAD
=======
from Main.Libraries.AirSpaceLib import buildAirSpace
from Main.Libraries.AirSpaceLib import buildAirGraf
from Main.Libraries.GraphLib import plot
from Main.Libraries.GraphLib import plotNode
from Main.Libraries.GraphLib import findShortestPath
from Main.Libraries.GraphLib import plotPath
>>>>>>> origin/main
""" ===========================================================================================
Program to test the airspace classes
"""
A = AirSpaceLib.buildAirSpace("Cat")
G = AirSpaceLib.buildAirGraf(A)
GraphLib.plot(G)
GraphLib.plotNode(G,"GODOX")
c = GraphLib.findShortestPath(G,"LEBL","LEZG")
GraphLib.plotPath(G,c)