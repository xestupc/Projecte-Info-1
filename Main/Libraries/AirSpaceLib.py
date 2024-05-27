import NavPointLib
import NavSegmentLib
import NavAirportLib
import NodeLib
import SegmentLib
import GraphLib
import PathLib

class AirSpace:
    def __init__(self):
        self.points = []
        self.segments = []
        self.airports = []

def addPoint(air, point):
    if point not in air.points:
        air.points.append(point)

def addSegment(air, numOrig, numDst, distance):
    np1 = next((point for point in air.points if point.num == numOrig), None)
    np2 = next((point for point in air.points if point.num == numDst), None)

    if not np1 or not np2:
        return

    ns1 = NavSegmentLib.NavSegment(np1, np2, float(distance))
    if ns1 not in air.segments:
        air.segments.append(ns1)

def addAirport(air, name):
    if not any(airport.name == name for airport in air.airports):
        air.airports.append(NavSegmentLib.NavAirport(name))

def addSID(air, nameAirport, nameSID):
    pointSID = next((point for point in air.points if point.name == nameSID), None)
    if not pointSID:
        return

    for airport in air.airports:
        if airport.name == nameAirport:
            if pointSID not in airport.sid:
                airport.sid.append(pointSID)
            break

def addSTAR(air, nameAirport, nameSTAR):
    pointSTAR = next((point for point in air.points if point.name == nameSTAR), None)
    if not pointSTAR:
        return

    for airport in air.airports:
        if airport.name == nameAirport:
            if pointSTAR not in airport.start:
                airport.start.append(pointSTAR)
            break

def loadNavPoints(air, filename):
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            if len(data) == 4:
                try:
                    addPoint(air, NavPointLib.NavPoint(data[0], data[1], float(data[2]), float(data[3])))
                except ValueError:
                    continue
    return air

def loadSegments(air, filename):
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            if len(data) == 3:
                try:
                    addSegment(air, data[0], data[1], float(data[2]))
                except ValueError:
                    continue
    return air

def loadAirports(air, filename):
    with open(filename, 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            addAirport(air, line)

            sid = file.readline().strip()
            addSID(air, line, sid)

            star = file.readline().strip()
            addSTAR(air, line, star)
    return air

def buildAirSpace(filename):
    air = AirSpace()
    air = loadNavPoints(air, filename + "_nav.txt")
    air = loadSegments(air, filename + "_seg.txt")
    air = loadAirports(air, filename + "_aer.txt")
    return air

def buildAirGraph(air):
    g = GraphLib.Graph()

    for point in air.points:
        g.addNode(NodeLib.Node(point.name, point.lon, point.lat))

    for seg in air.segments:
        g.addSegment(seg.orig.name, seg.dst.name)

    for airport in air.airports:
        if airport.sid and airport.start:
            sidName = airport.sid[0].name
            startName = airport.start[0].name

            neighbors = []
            for gNode in g.nodes:
                if gNode.name == sidName:
                    neighbors = gNode.neighbors[:]
                for neighbor in gNode.neighbors:
                    if neighbor.name == sidName or neighbor.name == startName:
                        neighbor.name = airport.name

            for gNode in g.nodes:
                if gNode.name == airport.name:
                    gNode.neighbors = neighbors

            for seg in g.segments:
                if seg.n1.name == sidName or seg.n1.name == startName:
                    seg.n1.name = airport.name
                if seg.n2.name == sidName or seg.n2.name == startName:
                    seg.n2.name = airport.name

    return g

def airportsToKML(air, nameFile):
    with open(nameFile, 'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        file.write('<Document>\n')

        for airport in air.airports:
            if airport.sid:
                file.write('  <Placemark>\n')
                file.write(f'    <name>{airport.name}</name>\n')
                file.write('    <Point>\n')
                file.write(f'      <coordinates>{airport.sid[0].lon},{airport.sid[0].lat}</coordinates>\n')
                file.write('    </Point>\n')
                file.write('  </Placemark>\n')

        file.write('</Document>\n')
        file.write('</kml>\n')

def AirSpaceRouting(air, airport1, airport2, nameFile):
    navAirport1 = next((airport for airport in air.airports if airport.name == airport1), None)
    navAirport2 = next((airport for airport in air.airports if airport.name == airport2), None)

    if not navAirport1 or not navAirport2:
        return

    g = buildAirGraph(air)

    for gNode in g.nodes:
        gNode.neighbors = [neighbor for neighbor in gNode.neighbors if neighbor.name not in [airport1, airport2]]

    p = GraphLib.findShortestPath(g, airport1, airport2)

    for n in p.nodes:
        if n.name in [airport1, airport2]:
            continue
        for airport in air.airports:
            if n.name == airport.name:
                return

    PathLib.pathToKML(p, nameFile)


