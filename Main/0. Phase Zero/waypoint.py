
import math
import numpy 

class WaypointClass():
    def __init__(self, latitude, longitude, waypoint_name):
        self.latitude = latitude
        self.longitude = longitude
        self.name = waypoint_name

def WaypointConstructor():
    test_waypoint = WaypointClass("", "", "")
    return test_waypoint

def LocateWaypoint(waypoint, lat, lon):
    waypoint.latitude = lat
    waypoint.longitude = lon
    
def NameWaypoint(waypoint,name):
    waypoint.name = name
    
def ShowWaypoint(wp):
    print(wp.latitude)
    print(wp.longitude)
    print(f"{wp.name}\n")

# Advanced Functions:

def CalculateDistanceWaypoint(wp1, wp2):
    # Calculates Haversine distance of the two points.
    # Degrees to radians (?)

    radius_sphere = 6335.439 # [km] at eq

    # Converts automatically to Radians. MUST INPUT IN DEGREES [º] !!!

    # print("Please take into account that when calculating distances, the latitudes and longites of your points MUST be entered in degrees [Dº].")
    # print("Otherwise, the calculations will be off. NOTE: The final Distance result will be in kilometers.")
    sigma_p1 = wp1.latitude * ((2 * math.pi) / 360)
    sigma_p2 = wp2.latitude * ((2 * math.pi) / 360)
    lambda_p1 = wp1.longitude * ((2 * math.pi) / 360)
    lambda_p2 = wp2.longitude * ((2 * math.pi) / 360)

    top_arrel_sumas = 1 - math.cos(sigma_p2 - sigma_p1) 
    top_arrel_mult = math.cos(sigma_p1) * math.cos(sigma_p2) * (1 - math.cos(lambda_p2 - lambda_p1))
    top_arrel = top_arrel_sumas + top_arrel_mult

    arrel = math.sqrt ( top_arrel / 2) 

    distance = 2 * radius_sphere * numpy.arcsin(arrel)
    return distance # in km

