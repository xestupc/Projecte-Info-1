class NavSegment:
    def __init__(self, orig, dst, dist):
        self.orig = orig
        self.dst = dst
        self.dist = dist

def NavSegmentFunc(orig, dst, dist):
    nav_segment = NavSegment(orig, dst, dist)
    return nav_segment

