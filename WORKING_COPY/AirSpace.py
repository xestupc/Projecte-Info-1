import graph
import NavPoint
import NavSegment
import NavAirport

'''
Airspace(Navpoint:[], NavSegments:[], NavAirports:[])
-----------------------------------------------------
Airspace(): Constructor. Defines class Airspace. Builds an empty AirSpace, without any point, segment or airport.

NavPoints: vector of NavPoint of the airspace.
NavSegments: vector of NavSegment of the airspace.
NavAirports: vector of NavAirports of the airspace.
'''
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



'''
Defines addPoint, which receives an AirSpace (air) and a NavPoint (point) and adds the navigation point to the airspace.

air: object of type 'AirSpace', represents the airspace where the navigation point will be added
point: object of type 'Navpoint', represents the navigation point to be added.

Returns: nothing
'''
def addPoint(air, point):
    # Add a navigation point to the airspace
    if point not in air.NavPoints:
        air.NavPoints.append(point)



'''
Defines addSegment, which receives an AirSpace (air), the numbers of two NavPoint (numOrig and numDst) and the distance between them and adds the segment to the airspace.

air: object of type 'Airspace', represents rhe airspace where the segment will be added.
numOrig: integer, identifier of the origin navigation point of the segment.
numDst: integer, identifier of the destination navigation point of the segment.
distance: float, distance between the origin and destination navigation points.

Returns: nothing
'''
def addSegment(air, numOrig, numDst, distance):
    # Add a segment between two navigation points with the given distance
    if (numOrig, numDst) not in [(s[0], s[1]) for s in air.NavSegments]:
        air.NavSegments.append((numOrig, numDst, distance))



'''
Defines addAirport, which receives an AirSpace (air) and the name (name) of an airport, and adds it to airspace.

air: object of type 'AirSpace', represents the airspace where the airport will be added.
name: string, name of the airport to be added.

Returns: nothing
'''
def addAirport(air, name):
    # Add an airport to the airspace
    if name not in air.NavAirports:
            air.NavAirports.append(name)



'''
Defines addSID, which receives an AirSpace (air) and the name (name) of an airport and the name of a navigation point (nameSID), and adds the take-off segment from the airport to the navigation point.

air: object of type 'AirSpace', represents the airspace where the take-off segment will be added.
nameAirport: string, name of the airport from which the take-off segment originates.
nameSID: string, name of the navigation point (SID) to which the take-off segment is directed.

Returns: nothing
'''
def addSID(air, nameAirport, nameSID):
    # Add a take off segment from an airport to a navigation point 
    if nameAirport in air.NavAirports:
        if nameSID in air.NavPoints:
            air.sids[nameAirport].append(nameSID)
        else:
            print("Error: El punto de navegación no existe")
    else:
        print("Error: El aeropuerto no existe")



'''
Defines addSTAR, which receives an AirSpace (air) and the name (name) of an airport and the name of a navigation point (nameSTAR), and adds the landing segment from the navigation point to the airport.

air: object of type 'AirSpace', represents the airspace where the landing segment will be added.
nameAirport: string, name of the airport to which the landing segment is directed.
nameSTAR: string, name of the navigation point (STAR) from which the landing segment originates.

Returns: nothing
'''
def addSTAR(air, nameAirport, nameSTAR):
    # Add a STAR (Standard Terminal Arrival Route) for the given airport
    if nameAirport in air.NavAirports:
        if nameSTAR in air.NavPoints:
            air.stars[nameAirport].append(nameSTAR)
        else:
            print("Error: El punto de navegación no existe")
    else: 
        print("Error: El aeropuerto no existe")



'''
defines loadNavPoints, which receives an AirSpace (air) and the name of a text file with the navigation points and adds them to the airspace.

air: object of type 'AirSpace', represents the airspace where the navigation points will be added.
filename: string,  name of the text file containing the navigation points.

Returns: the updated airspace object, the function reads the navigation points from the file and updates the air object with these points, then returns the modified air object.
'''                
def loadNavPoints(air, filename):
    # Load navigation points from a text file and add them to the airspace
    with open(filename, 'r') as file:
        for line in file:
            point = line.strip()  # Remove leading/trailing whitespace
            if point not in air.NavPoints:
                air.NavPoints.append(point)



'''
Defines loadSegments, which receives an AirSpace (air) and the name of a text file with the navigation segments and adds them to the airspace.

air: object of type 'AirSpace', represents the airspace where the navigation segments will be added.
filename: string, name of the text file containing the navigation segments.

Returns: the updated airspace object, the function reads the navigation segments from the file and updates the air object with these segments, then returns the modified air object.
'''
def loadSegments(self, filename):
    # Load segments between navigation points from a text file and add them to the airspace
    with open(filename, 'r') as file:
        for line in file:
            numOrig, numDst, distance = line.strip().split(',')  # Split line into components
            self.segments.append((numOrig, numDst, float(distance)))  # Convert distance to float



'''
Defines loadAirports, which receives an AirSpace (air) and the name of a text file with the airports and adds them to the airspace.

air: object of type 'AirSpace', represents the airspace where the airports will be added.
filename: string, name of the text file containing the airport names.

Returns: the updated airspace object, the function reads the airport names from the file and updates the air object with these airports, then returns the modified air object.
'''
def loadAirports(self, filename):
    # Load airport names from a text file and add them to the airspace
    with open(filename, 'r') as file:
        for line in file:
            airport = line.strip()  # Remove leading/trailing whitespace
            if airport not in self.airports:
                self.airports.append(airport)



'''
Defines buildAirSpace, a constructor. Receives the partial pathname of the files of an airspace, builds the airSpace and returns it.

filename: string, specifies the base filename used to construct the full filenames of the files containing navigation points, segments, and airports data.

Returns: an AirSpace object populated with data read from the files. The function constructs the AirSpace object and fills it with data from the files, then returns the populated object.
'''
def buildAirSpace(filename):
    airspace = Airspace([], [], [])  # Create an instance of the AirSpace class
    nav_file = filename + '_nav.txt'  # Filename for navigation points
    seg_file = filename + '_seg.txt'  # Filename for segments
    aer_file = filename + '_aer.txt'  # Filename for airports
      
    airspace.loadNavPoints(nav_file)  # Load navigation points
    airspace.loadSegments(seg_file)  # Load segments
    airspace.loadAirports(aer_file)  # Load airports
    return airspace  # Return the constructed AirSpace object



'''
Defines builfAirGraph, which receives an AirSpace (air) and makes a Graph from its content. From the lists of NavPoint, NavSegment and NavAirport, the function generates the corresponding lists of Node and Segment of the graph. Use the functions of previous classes when possible

air: object of type 'AirSpace', provides the data necessary to construct the graph

Returns: a graph representing the connectivity of the airspace, the function constructs the graph based on the provided airspace data and returns the resulting graph.
'''
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

# New Functions for Airspace.py in PHASE 4

def airportsToKML(air, nomFile):
    with open(nomFile, "r") as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        file.write('<Document>\n')

        for airports in air.NavAirports:
            file.write('<Placemark>\n')
            file.write('<name>' + airports + '</name>\n')
            file.write('<description>' + 'Airport' + '</description>\n')
            file.write('<Point>\n')
            file.write('<coordinates>' + air.points[airports] + '</coordinates>\n')
            file.write('</Point>\n')
            file.write('</Placemark>\n')

        file.write('</Document>\n')
        file.write('</kml>\n')

# Additional Functions for Airspace.py

def AirSpaceRouting(air, airport1, airport2, nomFile):
    # Check that the two numbers are the numbers of two airports in airspace
    if airport1 not in air.NavAirports or airport2 not in air.NavAirports:
        print("Error: Airport names do not exist in Airspace")
        return
    
    with open(nomFile, "r") as file:
        file.write("Shortest path between" + airport1 + "and" + airport2 + ":\n")
