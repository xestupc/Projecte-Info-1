'''
NavSegment(orig:integer, dst:integer, dist:float)
---------------------------------------
Defines class NavSegment, constructor. Build a NavSegment from two NavPoint (orig, dst) and the distance that separates them.

originNumber: number, the origin node number of the segment
destinationNumber: number, the destination node number of the segment
distance: number, effective distance in kilometers to go from origin to destination
'''

class NavSegment:
    def __init__(self, orig, dst, dist):
        self.orig = orig
        self.dst = dst
        self.dist = dist

def NavSegmentFunc(orig, dst, dist):
    nav_segment = NavSegment(orig, dst, dist)
    return nav_segment

