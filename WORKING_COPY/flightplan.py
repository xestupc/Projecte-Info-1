
import waypoint as wp
import matplotlib.pyplot as plt

class FlightPlanClass():
    def __init__(self, route, route_distance):
        self.route = route # (a vector of Waypoint, that the drone will follow in order, only one-way
        self.distance_total = route_distance # number


def FlightPlanConstructor():
    # creates and returns and empty FlightPlan object
    Obj_FlightPlan = FlightPlanClass([], "")
    return Obj_FlightPlan


def SetFpDeparture(fp, wp):
    if not fp.route:
        fp.route.append(wp)
        return 0
    else:
        fp.route.append(wp)
        return ((len(fp.route)) * -1)
    

def AddWaypointToFp(fp, wp):
    if not fp.route:
        fp.route.append(wp)
        return -1
    else:
        fp.route.append(wp)
        return 0


def ShowFlightPlan(fp):
    number = 1
    for item in fp.route:
        print(f"Waypoint number {number}")
        # num = fp.route.index(item) + 1 
        # print(f"\nWaypoint {num}")
        wp.ShowWaypoint(item)
        number += 1


# Advanced Functions: 
def FinishFlightPlan(fp):

    if fp.route == []:
        fp.distance_total = 0
        return -1
        # if empty the distance total is zero. obv

    else:
        SumDistances = 0
        indice = 0
        while indice < len(fp.route) - 1:
            distancia = wp.CalculateDistance(fp.route[indice], fp.route[indice + 1])
            SumDistances = SumDistances + distancia
            indice += 1
        fp.distance_total = SumDistances

        return SumDistances


def SearchWaypointByName(fp, name):
    # Loops over route of fp for Waypoint with a name.
    # Returns position of waypoint and -1 if not fownd.

    indice = 0
    name_found = False

    for item in fp.route:
        if fp.route[item] == name:
            indice = fp.route.index(item)
            name_found = True
            break
        return indice

    if name_found == False:
        return -1 
    

def PlotFlightPlan(fp):

    Vx = []
    Vy = []

    if fp.route == []: # If empty won't show any graphs
        return -1

    else:
        for item in fp.route:
            Vx.append(item.latitude)
            Vy.append(item.longitude)

        plt.plot(Vx, Vy)
        plt.show()

        return FinishFlightPlan(fp)
        # returns distance value, 0 if empty


def LoadFlightPlan(filename, fp):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split()
                if len(data) != 2:
                    continue  # Skip lines that don't have exactly 2 elements
                try:
                    latitude = float(data[0])
                    longitude = float(data[1])
                    # name = data[2]
                    fp.route.append(wp.WaypointClass(latitude, longitude, ""))
                except ValueError:
                    continue  # Skip lines where latitude or longitude couldn't be converted to float
        return len(fp.route) if len(fp.route) > 0 else 0  # Return the number of waypoints loaded into the flight plan, or 0 if no waypoints loaded
    except FileNotFoundError:
        return -1  # Return -1 if the file doesn't exist


def SearchWaypointByName(fp, name):
    # Loops over route of fp for Waypoint with a name.
    # Returns position of waypoint and -1 if not found.
    indice = -1
    name_found = False
    for i, item in enumerate(fp.route):
        if item == name:
            indice = i
            name_found = True
            break
    return indice


def IsPath(fp, name1, name2):
    # Check if FlightPlan is empty
    if not fp.route:
        return False
    # Find indices of name1 and name2
    index1 = SearchWaypointByName(fp, name1)
    index2 = SearchWaypointByName(fp, name2)

    if index1 == -1 or index2 == -1:
        return False

    if index1 == index2:
        return True

    if index1 < index2:
        return all(wp != '' for wp in fp.route[index1:index2])
    else:
        return all(wp != '' for wp in fp.route[index2:index1])