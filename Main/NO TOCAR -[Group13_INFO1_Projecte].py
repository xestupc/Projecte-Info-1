
# Llibreries externes
# =====================================================================================================================
import matplotlib as plt
import math as math

# Llibreries propies
# =====================================================================================================================

"""
import UI_imprv as colorin
import flightplan as fp
import waypoint as wp

import graph as graph
import node as node
import segment as segment
"""

# Misc
# General Utility Functions:
# =====================================================================================================================

def is_int(value):
    # See if input is a number to be converted to int
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_float(value):
    # See if input is a valid decimal number to be converted to float
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_string(value):
    # See if what you're typing is a string
    try:
        str(value)
        return True
    except ValueError:
        return False

def is_inside_list_length(lst, num):
    # Check if given input index is a valid one in regards to a list length
    try:
        if 0 <= num < len(lst):
            return True
        else:
            return False
    except TypeError:
        return False
    
def is_inside_of_a_given_list(list, value):
    # Check if a value is in fact inside of a given list
    try:
        for item in list:
            if value == item:
                return True
    except TypeError:
        return False
    

# Default values:
# =====================================================================================================================
# These are set every time the program is run (before the main loop)
# WIP !!!
"""
FlightPlanDefault = fp.FlightPlanConstructor()
FlightPlanDefault.route = []
FlightPlanDefault.distance_total = ""
"""
Exit_Program = False
list_of_possible_options = ["a","b","c","d","e","f","g","h","i","z"
                            ,'a','b','c','d','e','f','g','h','i','z']
    # Your input will always be a string, but just in case I'm leaving the charachters too.

# MAIN:
# =====================================================================================================================

print("\n\n\nWelcome to group's 13 INFO1 Project. We hope you find it to your liking.")
while Exit_Program == False:

    # Get desired option loop
    print("\n[ Menu ]")
    print(30 * "=")
    print("\nPlease choose between the following options in order to continue: \n")
    print("[a] - Load a simple Graph") # i.e the 1st week graph (??)
    print("[b] - Plot Graph")
    print("[c] - Plot a given node. ") # Ask for node name
    print("[d] - Plot a path from a list of nodes. ") # Ask for list of nodes to form the path
    print(30* "-")
    print("[e] - Plot minimum path between two given nodes. ") # Ask Origin and Destination Nodes
    print("[f] - Load Existing Airspace. ") # Ask for Airspace Name
    print("[g] - List Airports in memory. ")
    print("[h] - Create a Airports.kml file. ") # Ask name of the output file
    print("[i] - Create a route.kml file. ") # Ask name of the output file
    print("[j] - Find the route between 2 airports. ")
    print(30* "-")
    print("[z] -- [Exit]")

    # Input option is made sure to be valid (one of the accepted strings / char) and sent forward if so, 
    # else will keep looping
    chosen_option_entry = input("\nPlease enter your chosen feature: ")
    while is_inside_of_a_given_list(list_of_possible_options, chosen_option_entry) == False: 
        print("Wrong input type. Try again. Make sure to choose an existing feature.")
        chosen_option_entry = input("Please enter your chosen feature: ")

    # Debug feature -- REMOVE LATER
    if is_inside_of_a_given_list(list_of_possible_options, chosen_option_entry) == True:
        print("Working as intended.")
    
    chosen_option = (chosen_option_entry).lower()
    print(type(chosen_option))
    print("\n")

    # Option Code
    # ---------------------------------------------------------------------------------------------------------------------

    # Notes: 
    # When loading from a file I've not taken into account file writing errors YET. 

    if chosen_option == "a":
    # a = "Load a simple Graph"

        print("You've chosen to Load an Existing Graph. Before loading the file, we must ask you something.")
        print("Make sure that the data file follows one of these formats.")
        print("Option 1. (simple written .txt file):")
        print(" - Node Format:  [Node Name] [Latitude] [Longitude] ")
        print(" - Segment Format: [Origin_Node_Name] [Destination_Node_Name]")
        print("Option 2 (Following the 'Cat_nav.txt' example):")
        print(" - Node Format: [Num] [Loc.X] [Latitude] [Longitude].")
        print(" - Segment Format: ")
        entered_format = input("Choose a format: ")
        # Option must be 1 or 2:
        # I can either condition for it to be inside list_lenght and int or just 1 / 2

        while is_int(entered_format) == False and (entered_format != 1 or entered_format !=2):
            print("Wrong input type. Please try again.")
            entered_format = input("Enter your format choice: ")
        
        graphToLoad = graph.GraphClass([], [])

        if int(entered_format) == 1:

            graph_file_path = input("Enter a path for your graph file. Make sure python has acces to it. ")
            # Name Lat Lon

            try:
                 with open(graph_file_path, 'r') as graphFile:
                    lines = graphFile.readlines()
                    for line in lines:
                        node_data = line.strip().split()
                        if len(node_data) !=3:
                            continue # Skips non - 3 elements 
                        try:
                            node_name = str(node_data[0])
                            node_latitude = float(node_data[1])
                            node_longitude = float(node_data[2])
                            graphToLoad.nodes.append(node.NodeClass(node_name, node_latitude, node_longitude))
                        except ValueError:
                            continue
            except FileNotFoundError:
                print("Something went wrong. File not found. Check path / permissions and try again. ")
                            

            graphToLoad.nodes
            graphToLoad.segments


        if int(entered_format) == 2:
            graph_file_path = input("Enter a path for your graph file. Make sure python has acces to it. ")
            # Num X Lat Lon

    # LOGIC: 

    # ERROR CONDITIONS:
    # Graph must exist
    # Graph must not be empty
    # Path must be valid: Have acces (NO DESKTOP (?))

    elif chosen_option == "b":
    # b = "Plot Graph"

    # LOGIC: 

    # ERROR CONDITIONS:
    # Graph must exist
    # Graph must not be empty
    # Graph name must be valid / correspond
       
    elif chosen_option == "c":
    # c = "Plot Node" --> Ask for Node Name
      
    # LOGIC: 

    # ERROR CONDITIONS:
    # Node must exist
    # Name must be valid / correspond

    elif chosen_option == "d":
    # d = "Plot Path" --> Ask for list of Nodes to form Path

    # LOGIC: 

    # ERROR CONDITIONS:
    # Both nodes must exist
    # A Path must be possible between the two
    # If they are Both the same position Path is "", should we plot? Ask the user. 
    # Input list must be valid

# =====================================================================================================================



    elif chosen_option == "e":
    # e = "Plot minimum Path" --> Ask Origin and Destination Nodes

    # LOGIC: 

    # ERROR CONDITIONS:
    # Both origin and destination nodes must exist
    # Their names must correspond to something
    # If they are the same node ask if plot empty path
       
    elif chosen_option == "f":
    # f = "Load Airspace" --> Ask Airspace Name

    # LOGIC: 

    # ERROR CONDITIONS:
    # Airspace must exist
    # Airspace must not be empty
    # Input name must be correct / correspond
    
    elif chosen_option == "g": 
    # List Airports

    # LOGIC: 

    # ERROR CONDITIONS:
    # Empty list --> Error message
      
    elif chosen_option == "h":
    # h = "Create Airpots.kml" --> Ask Name of the Output file

    # LOGIC: 

    # ERROR CONDITIONS:
    # Invalid path 
    # Empty file

    elif chosen_option == "i":
    # i = "Create Route.kml" --> Ask Name of the Output file

    # LOGIC: 

    # ERROR CONDITIONS:
    # Invalid path 
    # Empty file
       
    elif chosen_option == "j": 
    # j = "Find a Route Between 2 Airports" 

    # LOGIC: 

    # ERROR CONDITIONS:
    # Invalid path 
    # They both must exist
    # If same --> say something
    


    elif chosen_option == "z":
        Exit_Program = True
        print("You've chosen to exit the program. Restart to run it again.")
        print("Until we see you again.")


    else:
        print("Unknown option. Try again.")


        



# Phase Three


# Phase Four
