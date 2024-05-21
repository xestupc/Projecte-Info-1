class NavPoint():
    def __init__ (self, num, name, lat, lon):
        self.number=num
        self.name=name
        self.latitude=lat
        self.longitude=lon

def NavPointfunc (num, name, lat, lon):
    Navpoint = NavPoint("", "", "", "")
    return Navpoint