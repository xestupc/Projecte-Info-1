
import AirSpace
import NavAirport
import NavSegment
import graph

A = AirSpace.buildAirSpace("Cat")
G = AirSpace.buildAirGraf(A)
graph.plot(G)
graph.plotNode(G,"GODOX")
c = graph.findShortestPath(G,"LEBL","LEZG")
graph.plotPath(G,c)