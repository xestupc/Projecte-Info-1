import graph
import NavPoint
import NavSegment
import NavAirport

class Airspace():
    def __init__(self, NavPoints, NavSegments, NavAirports):
        self.NavPoints = NavPoints
        self.NavSegments = NavSegments
        self.NavAirports = NavAirports

def buildAirspace(filename):
    Nav = f"C:\Transport Aeri Q2\{filename}_nav.txt"
    Seg = f"C:\Transport Aeri Q2\{filename}_seg.txt"
    Air = f"C:\Transport Aeri Q2\{filename}_aer.txt"
    newAirspace = Airspace(Nav, Seg, Air)
    return newAirspace


def addSegment(air, numOrig, numDst, distance):
    # Add a segment between two navigation points with the given distance
    if (numOrig, numDst) not in [(s[0], s[1]) for s in air.NavSegments]:
        air.NavSegments.append((numOrig, numDst, distance))

def addAirport(air, name):
    # Add an airport to the airspace
    if name not in air.NavAirports:
            air.NavAirports.append(name)

def addSID(air, nameAirport, nameSID):
    # Add a take off segment from an airport to a navigation point 
    if nameAirport in air.NavAirports:
        if nameSID in air.NavPoints:
            air.sids[nameAirport].append(nameSID)
        else:
            print("Error: El punto de navegación no existe")
    else:
        print("Error: El aeropuerto no existe")

def addSTAR(air, nameAirport, nameSTAR):
    # Add a STAR (Standard Terminal Arrival Route) for the given airport
    if nameAirport in air.NavAirports:
        if nameSTAR in air.NavPoints:
            air.stars[nameAirport].append(nameSTAR)
        else:
            print("Error: El punto de navegación no existe")
    else: 
        print("Error: El aeropuerto no existe")
                 
           
def loadNavPoints(air, filename):
    # Load navigation points from a text file and add them to the airspace
    with open(filename, 'r') as file:
        for line in file:
            point = line.strip()  # Remove leading/trailing whitespace
            if point not in air.NavPoints:
                air.NavPoints.append(point)

def loadSegments(self, filename):
    # Load segments between navigation points from a text file and add them to the airspace
    with open(filename, 'r') as file:
        for line in file:
            numOrig, numDst, distance = line.strip().split(',')  # Split line into components
            self.segments.append((numOrig, numDst, float(distance)))  # Convert distance to float

def loadAirports(self, filename):
    # Load airport names from a text file and add them to the airspace
    with open(filename, 'r') as file:
        for line in file:
            airport = line.strip()  # Remove leading/trailing whitespace
            if airport not in self.airports:
                self.airports.append(airport)

def buildAirSpace(filename):
    # Construct an AirSpace object by loading data from three files based on the provided filename
    airspace = Airspace([], [], [])  # Create an instance of the AirSpace class
    nav_file = filename + '_nav.txt'  # Filename for navigation points
    seg_file = filename + '_seg.txt'  # Filename for segments
    aer_file = filename + '_aer.txt'  # Filename for airports
      
    airspace.loadNavPoints(nav_file)  # Load navigation points
    airspace.loadSegments(seg_file)  # Load segments
    airspace.loadAirports(aer_file)  # Load airports
    return airspace  # Return the constructed AirSpace object

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