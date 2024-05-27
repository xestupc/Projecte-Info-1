
# Llibreries externes
# =====================================================================================================================
import matplotlib as plt
import math as math

import sys
import os

# Llibreries propies
# =====================================================================================================================


from Main.Libraries import AirSpaceLib, FlightplanLib, GraphLib, NavAirportLib, NavPointLib, NavSegmentLib, NodeLib, PathLib, SegmentLib, WaypointLib
from Main.Misc import UI_imprv as UI_Lib


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

# Empty Graph and Airspace Objects

graphToOperate = graph.GraphClass([], [])
airspaceToOperate = Airspace.Airspace([], [], [])

Exit_Program = False
list_of_possible_options = ["a","b","c","d","e","f","g","h","i","z"
                            ,'a','b','c','d','e','f','g','h','i','z']
# Your input will always be a string, but just in case I'm leaving the chars too.

# MAIN:
# =====================================================================================================================

menu = r"""
 __  __ ______ _   _ _    _ 
|  \/  |  ____| \ | | |  | |
| \  / | |__  |  \| | |  | |
| |\/| |  __| | . ` | |  | |
| |  | | |____| |\  | |__| |
|_|  |_|______|_| \_|\____/  """

print("\n\n\nWelcome to group's 13 INFO1 Project. We hope you find it to your liking.")
while Exit_Program == False:

    # Get desired option loop
    
    print(menu)
    print(30 * "=")
    print("Please choose between the following options in order to continue: \n")
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

        load_new_graph = False
        if len(graphToOperate.nodes) == 0 and len(graphToOperate.segments) == 0:
            load_new_graph = True
            # if graph is empty == "does not exist / not loaded" it will load a new one, to be used in next statements
        else:
            print("A graph is already loaded. Are you sure you wish to continue?")
            if input("Write 'YES' or 'NO': ").lower() == 'yes':
                load_new_graph = True
                print("Previous data will be deleted.")
            # if it already exists, we can either keep or delete the old one


        if load_new_graph == True:

            graphToOperate = GraphLib.GraphClass([], [])

            print("You've chosen to Load an Existing Graph. Before loading the file, we must ask you something.")
            print("Make sure that the data file follows one of these formats.")
            print("Option 1. (simple written .txt file):")
            print(" - Node Format:    [Node Name] [Latitude] [Longitude] ")
            print(" - Segment Format: [Origin Node Name] [Destination Node Name]")

            print("Option 2 (Following the 'Cat_nav.txt' example):")
            print(" - Node Format:    [Num / Name] [Loc.X] [Latitude] [Longitude].")
            print(" - Segment Format: [Origin Node Name] [Destination Node Name] [Segment Cost]")
            print("Notes: If any given nodes have some kind of ")
            entered_format = input("Choose a format: ")
            # Option must be 1 or 2:
            # I can either condition for it to be inside list_lenght and int or just 1 / 2

            while is_int(entered_format) == False and (entered_format != 1 or entered_format !=2):
                print("Wrong input type. Please try again.")
                entered_format = input("Enter your format choice: ")

            if int(entered_format) == 1:

                graph_file_path = input("Enter a path for your graph file. Make sure python has acces to it. ")
                # Name Lat Lon

                # if BOTH nodes are inside of their given lists (that is the graph.nodes list)
                # for this to work we FIRST add the nodes and then the segments

                try:
                     with open(graph_file_path, 'r') as graphFile:
                        lines = graphFile.readlines()
                        for line in lines:
                            node_data = line.strip().split()
                            if len(node_data) != 3:
                                continue # Skips non 3 elements i.e non nodes or error type                       
                            try:
                                node_name = str(node_data[0])
                                node_latitude = float(node_data[1])
                                node_longitude = float(node_data[2])
                                graphToOperate.nodes.append(NodeLib.NodeClass(node_name, node_latitude, node_longitude))

                            except ValueError:
                                continue

                except FileNotFoundError:
                    print("Something went wrong. File not found. Check path / permissions and try again. ")


                try:
                     with open(graph_file_path, 'r') as graphFile:
                        lines = graphFile.readlines()
                        for line in lines:
                            node_data = line.strip().split()
                            if len(node_data) != 2:
                                continue # Skips non 2 elements i.e non segments or error type                       
                            
                            if is_inside_of_a_given_list(graphToOperate.nodes, node_data[0]) == True and is_inside_of_a_given_list(graphToOperate.nodes, node_data[1]) == True:
                                # If [name origin] [name destination] BOTH exist create segments for each and add them to the graph
                                try:
                                    node_origin = str(node_data[0])
                                    node_destination = str(node_data[1])
                                    graphToOperate.segments.append(SegmentLib.SegmentFunc(node_origin, node_destination))

                                except ValueError:
                                    continue
                except FileNotFoundError:
                    print("Something went wrong. File not found. Check path / permissions and try again. ")


            if int(entered_format) == 2:

                graph_file_path = input("Enter a path for your graph file. Make sure python has acces to it. ")
                # Num X Lat Lon. Whole code very similar to option 1.

                # if BOTH nodes are inside of their given lists (that is the graph.nodes list)
                # for this to work we FIRST add the nodes and then the segments

                try:
                     with open(graph_file_path, 'r') as graphFile:
                        lines = graphFile.readlines()
                        for line in lines:
                            node_data = line.strip().split()
                            if len(node_data) != 4:
                                continue # Skips non 4 elements i.e non nodes or error type                       
                            try:
                                node_name = str(node_data[0])
                                # We ignore node data (1) as its LOC_X and we dont need it.
                                node_latitude = float(node_data[2])
                                node_longitude = float(node_data[3])
                                graphToOperate.nodes.append(NodeLib.NodeClass(node_name, node_latitude, node_longitude))

                            except ValueError:
                                continue
                except FileNotFoundError:
                    print("Something went wrong. File not found. Check path / permissions and try again. ")


                try:
                     with open(graph_file_path, 'r') as graphFile:
                        lines = graphFile.readlines()
                        for line in lines:
                            node_data = line.strip().split()
                            if len(node_data) != 2:
                                continue # Skips non 2 elements i.e non segments or error type                       
                            
                            if is_inside_of_a_given_list(graphToOperate.nodes, node_data[0]) == True and is_inside_of_a_given_list(graphToOperate.nodes, node_data[1]) == True:
                                # If [name origin] [name destination] BOTH exist create segments for each and add them to the graph
                                try:
                                    node_origin = str(node_data[0])
                                    node_destination = str(node_data[1])
                                    node_cost = float(node_data[2])

                                    graphToOperate.segments.append(SegmentLib.SegmentClass(node_origin, node_destination, node_cost))

                                except ValueError:
                                    continue
                except FileNotFoundError:
                    print("Something went wrong. File not found. Check path / permissions and try again. ")

    # Checked ERROR CONDITIONS:
        # Graph must exist
        # Graph must not be empty
        # Path must be valid: Have acces (NO DESKTOP (?)) --> if no error when opening file we're good

    elif chosen_option == "b":
    # b = "Plot Graph"
    # We first must check that a graph has been loaded, i.e it ain't empty

        if graphToOperate.nodes == []:
            print("The Graph you're trying to plot is empty. Make sure to have loaded a Graph before trying to plot one.")

        else:
            GraphLib.Plot(graphToOperate)

        # Checked ERROR CONDITIONS:
        # Graph must exist = not be empty
       
    elif chosen_option == "c":
    # c = "Plot Node" --> Ask for Node Name

        input("Before choosing a node to plot, do you wish to see those available?")
        node_to_plot_name = str(input("Please choose a valid node to plot."))
      
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


        



