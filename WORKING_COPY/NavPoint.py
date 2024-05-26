
'''
Navpoint(num: integer, name: str, lat: float, lon: float)
----------------------------------------------------------
Defines class NavPoint, is a constructor. Builds a NavPoint based on its number, its name, its latitude and its longitude.

number: number, the node number in the nav.txt file
name: string, name of the point
latitude: number, geographical latitude, in degrees
longitude: number, geographical longitude, in degrees
'''
class NavPoint():
    def __init__ (self, num, name, lat, lon):
        self.number=num
        self.name=name
        self.latitude=lat
        self.longitude=lon

def NavPointfunc (num, name, lat, lon):
    Navpoint = NavPoint("", "", "", "")
    return Navpoint

