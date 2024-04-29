
import waypoint as wp
import fightplan as fp
import UI_imprv as clr

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_string(value):
    try:
        str(value)
        return True
    except ValueError:
        return False

def is_inside_list_length(lst, num):
    try:
        if 0 <= num < len(lst):
            return True
        else:
            return False
    except TypeError:
        return False

# Defaults
FlightPlanDefault = fp.FlightPlanFunc()
FlightPlanDefault.route = []
FlightPlanDefault.distance_total = ""
Exit_Program = False

# MAIN:

print("\n\n\nWelcome to group's 13 Phase Zero Test for the Informatica 1 project. We hope you find our program enjoyable.")

while Exit_Program == False:
    # get option --> to be used on elif statements 

    print("\nPlease choose between the following options in order to continue: \n")
    print("1. Create a Waypoint and add to a new FlightPlan.")
    print("2. Create a Waypoint and add to the existing FlightPlan.")
    print("3. Finish the FlightPlant and show the total distance.")
    print("4. Load FlightPlan from a file.")
    print("5. Show the FlightPlan.")
    print("6. Plot the FlightPlan.")
    print("7. Check if a path exists in the FlighPlan")
    print("8. Print a particular waypoint")
    print("9. Delete a given waypoint.")
    print("0. [Exit]")

    # 3 more features would be dope 

    chosen_option_entry = input("\nPlease enter your chosen feature: ")
    while is_int(chosen_option_entry) == False: 
        print("Wrong input type. Try again")
        chosen_option_entry = input("Please enter your chosen feature: ")
        
    chosen_option = int(chosen_option_entry)
    print("\n")
    
    if chosen_option == 1:

        create_new_flightplan = False
        if len(FlightPlanDefault.route) == 0:
            create_new_flightplan = True
        else:
            print("A flightplan already exists. Are you sure you wish to continue?")
            if input("Write 'YES' or 'NO': ") == 'yes' or 'YES':
                create_new_flightplan = True
                print("Previous data will be deleted.")
            #else: create_new_flightplan = False REDUNDANT !


        if create_new_flightplan == True:
            FlightPlanDefault.route = []
            FlightPlanDefault.distance_total = ""
            # FlightPlanDefault_Name = 

            new_waypointlat_entrada = input("Please choose a latitude for this new waypoint: ")
            while is_float(new_waypointlat_entrada) == False: 
                print("Wrong input type. Try again")
                new_waypointlat_entrada = input("Please choose a latitude for this new waypoint: ")
            new_waypointlat = float(new_waypointlat_entrada)
            

            new_waypointlon_entrada = input("Please choose a longitude for this new waypoint: ")
            while is_float(new_waypointlon_entrada) == False: 
                print("Wrong input type. Try again")
                new_waypointlon_entrada = input("Please choose a longitude for this new waypoint: ")
            new_waypointlon = float(new_waypointlon_entrada)


            new_waypoint_name = input("Finally, give it a name: ")

            new_waypoint = wp.WaypointClass(new_waypointlat, new_waypointlon, new_waypoint_name)
            FlightPlanDefault.route.append(new_waypoint)

            print("New waypoint succesfully added as the ORIGIN of your flightplan.")

        else: 
            print("You seem to want to add a new waypoint on the existing flightplan. Choose option '2' next if that's the case.")


    elif chosen_option == 2:
        
        if len(FlightPlanDefault.route) != 0:

            new_waypointlat_entrada = input("Please choose a latitude for this new waypoint: ")
            while is_float(new_waypointlat_entrada) == False: 
                print("Wrong input type. Try again")
                new_waypointlat_entrada = input("Please choose a latitude for this new waypoint: ")
            new_waypointlat = float(new_waypointlat_entrada)
            

            new_waypointlon_entrada = input("Please choose a longitude for this new waypoint: ")
            while is_float(new_waypointlon_entrada) == False: 
                print("Wrong input type. Try again")
                new_waypointlon_entrada = input("Please choose a longitude for this new waypoint: ")
            new_waypointlon = float(new_waypointlon_entrada)


            new_waypoint_name = input("Finally, give it a name: ")

            while fp.SearchWaypointByName(FlightPlanDefault, new_waypoint_name) != -1:
                print("This name already exists. Choose another one.")
                new_waypoint_name = input("Finally, give it a name: ")

            new_waypoint = wp.WaypointClass(new_waypointlat, new_waypointlon, new_waypoint_name)
            FlightPlanDefault.route.append(new_waypoint)

            print("New waypoint succesfully added.")

        else:
            print("There is no existing flightplan. Can't continue. Choose option 1 to create a new one.")


    elif chosen_option == 3:

        
        distance_total = fp.FinishFlightPlan(FlightPlanDefault)
        if distance_total == -1:
            print("The FlightPlan is empty. Make sure to add some Waypoints before trying to print anything. ")
        else:
            print("Please take into account that when calculating distances, the latitudes and longites of your points MUST be entered in degrees [Dº].")
            print("Otherwise, the calculations will be off. NOTE: The final Distance result will be in kilometers.\n")
            print(distance_total)


    elif chosen_option == 4:

        print("Got it. Make sure to open a valid file type and place it an accessible directory." )
        path_file_name = input("Please enter the file path you wish to load: ")
  
        result = fp.LoadFlightPlan(path_file_name, FlightPlanDefault)
        if result == 0:
            print("No waypoints have been loaded. Please make sure it isn't empty.")
        elif result == -1:
            print("The file does not exist. Check spelling if you believe this is a mistake.")
        else:
            print(f"A total of {result} waypoints have been loaded correctly.")
            # must check fp.LoadFlightPlan line 113. Append method as a waypoint not sure if correct.
    

    elif chosen_option == 5:

        if FlightPlanDefault.route == []:
            print("The flightplan is empty. No data stored to print.")

        else:
            fp.ShowFlightPlan(FlightPlanDefault)
            print(f"And the total distance is: {fp.FinishFlightPlan(FlightPlanDefault)}")
            # check if it prints correcrly. Otherwise print the "waypoint number x" in a while loop.


    elif chosen_option == 6:

        if FlightPlanDefault.route == []:
            print("The flightplan is empty. No data stored to plot.")

        else:
            fp.PlotFlightPlan(FlightPlanDefault)
            print(f"And the total distance is: {fp.FinishFlightPlan(FlightPlanDefault)}")
            # d here necessary ?


    elif chosen_option == 7: 
        if FlightPlanDefault.route == []:
            print("The flightplan is empty. No path to check for.")

        else: 
        
            nom1 = input("Waypoint 1: ")
            nom2 = input("Waypoint 2: ")

            if fp.IsPath(nom1 , nom2) == True:
                print("A path exists.")

            else:

                print("A path does not exist in the current flightplan. Check your inputs again if you think this is a mistake.")


    elif chosen_option == 8:

        index_to_print = 0
        if FlightPlanDefault.route == []:
            print("It seems that the FlightPlan is empty. Please add some waypoints before printing it.")
            
        else:
            index_to_print_entrada = input("Please choose a Waypoint to print. Give a number for it's position. From 1 being the first to X [depending on the amount of waypoints] being the last: ")


            while True:
                while is_int(index_to_print_entrada) == False:
                    print("Wrong input type. Try again")
                    index_to_print_entrada = input("Please choose a Waypoint to print: ")
                index_to_print = int(index_to_print_entrada) - 1


                if is_inside_list_length(FlightPlanDefault.route, index_to_print) == True:
                    print(f"You've chosen to print the Waypoint number {index_to_print} in your flightplan. It contains the following data: ")

                    if index_to_print == 0:
                        print(f"\nOrigin Waypoint: Latitude: {FlightPlanDefault.route[index_to_print].latitude}, Longitude: {FlightPlanDefault.route[index_to_print].longitude}, Name: {FlightPlanDefault.route[index_to_print].name}")
                    elif index_to_print == len(FlightPlanDefault.route):
                        print(f"\nDestiny Waypoint: Latitude: {FlightPlanDefault.route[index_to_print].latitude}, Longitude: {FlightPlanDefault.route[index_to_print].longitude}, Name: {FlightPlanDefault.route[index_to_print].name}")
                    elif 0 <= index_to_print < len(FlightPlanDefault.route):
                        wp.ShowWaypoint(FlightPlanDefault.route[index_to_print])

                    break

                else:
                    print("Wrong index. Try again")
                    index_to_print_entrada = input("Please choose a Waypoint to print: ")

         
        # for item in FlightPlanDefault.route:
        #     if item == FlightPlanDefault.route[0]:
        #         
        #     elif item == FlightPlanDefault.route[len(FlightPlanDefault.route)]:
        #         
        #     else:
        #         print(f"\nWaypoint number: {item.latitude}, Longitude: {item.longitude}, Name: {item.name}")
        #     index_to_print += 1
        # as of 29/4 i dont remember what this was for


    elif chosen_option == 9:
        if FlightPlanDefault.route == []:
            print("The FlightPlan is empty. Make sure to add waypoints first in order to delete them at a later time. ")
        else:
            waypoint_to_delete_entrada = input("Choose a waypoint to delete its info. From 1 being the first to X [depending on the amount of waypoints] being the last: ")
            while not waypoint_to_delete_entrada.isdigit() or int(waypoint_to_delete_entrada) < 1 or int(waypoint_to_delete_entrada) > len(FlightPlanDefault.route):
                print("Wrong input type or non-existing Waypoint. Try again. ")
                waypoint_to_delete_entrada = input("Please choose a Waypoint to delete: ")
            waypoint_to_delete = int(waypoint_to_delete_entrada) - 1  

            borrar = input("Are you sure? This is irreversible. ")
            if borrar.lower() == "yes":
                FlightPlanDefault.route.pop(waypoint_to_delete)
                print("Chosen waypoint has been deleted. Remember to update your index inputs when using other options.")
            else: 
                print("Okay. Waypoint data preserved.")


    elif chosen_option == 0:
        Exit_Program = True
        print("You've chosen to exit the program. Restart to run it again.")
        print("Until we see you again.")


    else:
        print("Unknown option. Try again.")
