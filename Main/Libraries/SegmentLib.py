
import NodeLib as node

class SegmentClass():
    def __init__(self, origin, destination, cost):
        self.origin = origin
        self.destination = destination
        self.cost = cost

def SegmentFunc(n1, n2):
    distance = node.Distance(n1, n2)
    Obj_segment = SegmentClass(n1, n2, distance)
    node.addNeighbor(n1, n2)
    return Obj_segment