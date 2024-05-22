import GraphClass
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



