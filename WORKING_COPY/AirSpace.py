import GraphClass
import NavPoint
import NavSegment
import NavAirport

class Airspace():
    def __init__(self, NavPoints, NavSegments, NavAirports):
        self.NavPoints = NavPoints
        self.NavSegments = NavSegments
        self.NavAirports = NavAirports



<<<<<<< HEAD
class AirSpace:
    def __init__(self):
        self.points =[] #List to store navigation points
        self.segments = [] #List to store segments between navigation points
        self.airports = [] # List to store airport names
        self.sids = {} # Dictionary to store SIDs (Standard Instrument Departures) for each airport
        self.stars = {} # Dictionary to store STARs (Standard Terminal Arrivals) for each airport


    def addPoint(self, point):
        # Add a navigation point to the airspace
        self.points.append(point)

    def addSegment(self, numOrig, numDst, distance):
        # Add a segment between two navigation points with the given distance
        self.segments.append((numOrig, numDst, distance))

    def addAirport(self, name):
        # Add an airport to the airspace
        self.airports.append(name)

    def addSID(self, nameAirport, nameSID):
        # Add a SID (Standard Instrument Departure) for the given airport
        if nameAirport in self.sids:
            self.sids[nameAirport].append(nameSID)
        else:
            self.sids[nameAirport] = [nameSID]

    def addSTAR(self, nameAirport, nameSTAR):
        # Add a STAR (Standard Terminal Arrival Route) for the given airport
        if nameAirport in self.stars:
            self.stars[nameAirport].append(nameSTAR)
        else:
            self.stars[nameAirport] = [nameSTAR]

    def loadNavPoints(self, filename):
        # Load navigation points from a text file and add them to the airspace
        with open(filename, 'r') as file:
            for line in file:
                point = line.strip()  # Remove leading/trailing whitespace
                if point not in self.points:
                    self.points.append(point)

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

    def buildAirSpace(cls, filename):
        # Construct an AirSpace object by loading data from three files based on the provided filename
        airspace = cls()  # Create an instance of the AirSpace class
        nav_file = filename + '_nav.txt'  # Filename for navigation points
        seg_file = filename + '_seg.txt'  # Filename for segments
        aer_file = filename + '_aer.txt'  # Filename for airports
        airspace.loadNavPoints(nav_file)  # Load navigation points
        airspace.loadSegments(seg_file)  # Load segments
        airspace.loadAirports(aer_file)  # Load airports
        return airspace  # Return the constructed AirSpace object




def buildAirGraph(air):
    
=======
>>>>>>> 4f057c16851d9184b04d58c15244949b5603c990
