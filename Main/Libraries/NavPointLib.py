class NavPoint():
    def __init__(self, num, name, lat, lon):
        self.num = num
        self.name = name
        self.lat = lat
        self.lon = lon


def NavPointFunc(num, name, lat, lon):
    nav_point = NavPoint(num, name, lat, lon)
    return nav_point

