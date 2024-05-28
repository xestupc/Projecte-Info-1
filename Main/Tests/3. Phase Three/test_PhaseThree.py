from Libraries import AirSpaceLib, Flightplan, GraphLib, NavAirportLib, NavPointLib, NavSegmentLib, NodeLib, PathLib, SegmentLib,WaypointLib

""" ===========================================================================================
Program to test the airspace classes
"""
A = AirSpace.buildAirSpace("Cat")
G = AirSpace.buildAirGraf(A)
graph.plot(G)
graph.plotNode(G,"GODOX")
c = graph.findShortestPath(G,"LEBL","LEZG")
graph.plotPath(G,c)