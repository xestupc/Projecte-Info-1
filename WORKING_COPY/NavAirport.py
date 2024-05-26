
'''
Navairport(name:string)
------------------------
Navairport(): constructor, defines NavAirport class.  Build an airport, from its name.

name: string, specifies the name of the airport to be constructed.
'''

class NavAirport():
    def __init__(self, name):
        self.name = name

def NavAirportFunc(name):
    nav_airport = NavAirport(name)
    return nav_airport  
