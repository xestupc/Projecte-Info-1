<<<<<<< HEAD
import NavPoint as NP

class NavSegment():
    def __init__ (self, NP1, NP2, dist):
        self.origin=NP1
        self.destination=NP2
        self.distance=dist

def NavSegmentfunc (NP1, NP2, dist):
    Navsegment = NavSegment("", "", "")
    return Navsegment
=======
class NavSegment:
    def __init__(self, orig, dst, dist):
        self.orig = orig
        self.dst = dst
        self.dist = dist

def NavSegmentFunc(orig, dst, dist):
    nav_segment = NavSegment(orig, dst, dist)
    return nav_segment

>>>>>>> origin/main
