import graph
import NavPoint
import NavSegment
import NavAirport

class Airspace():
    def __init__(self, NavPoints, NavSegments, NavAirports):
        self.NavPoints = NavPoints
        self.NavSegments = NavSegments
        self.NavAirports = NavAirports

def buildAirGraph(air):

    graph = graph.GraphClass()

# Create nodes for NavPoints and NavAirports
    for nav_point in air.nav_points:
     node = graph.addNode(nav_point.id, nav_point.coordinates)

    for nav_airport in air.nav_airports:
        sid = nav_airport.getSIDs()[0]
        coordinates = sid.getCoordinates()
        node = graph.addNode(nav_airport.id, coordinates)

# Create segments for NavSegments
    for nav_segment in air.nav_segments:
        node1 = graph.getNode(nav_segment.start_id)
        node2 = graph.getNode(nav_segment.end_id)
        segment = graph.addSegment(node1, node2)
        
    return graph

