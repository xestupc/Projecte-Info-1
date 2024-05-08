# Projecte-Info-1

Purpose: 

Build a data model (classes) representing a route network from the air, allowing us to find the minimum distance path between one place and another one.

Grading criteria: ATENEA pdf.

Phase Zero: Warmup mini project.

Files:

    1. Waypoint --> Class and functions (basic and advanced)
    2. Flightplan --> Class and basic (basic and advanced)
    3. test_Waypoint --> Check Code individually
    4. test_Flighplan --> Check Code individually
    5. test_phaseZERO --> Code Works Entirely. Check Criteria


Classes and Functions: 

    Waypoint:

        Waypoint Class
        - Latitude (number)
        - Longitude (number)
        - Waypoint name (text)

        Waypoint()
        - Input: None.
        - Output: Empty Waypoint class object
        Description: Constructor.


        LocateWaypoint(wp, lat, lon)
        - Input: One Waypoint and two Numbers
        - Output: None.
        Description: Sets attributes lotitude and longitude.

        NameWaypoint(wp, name)
        - Input: One Waypoint and one String
        - Output: None.
        Description: Sets attributes name.

        ShowWaypoint(wp)
        - Input: One Waypoint 
        - Output: None.
        Description: Shows WP information on screen.


        "ADV":

        CalculateDistance(wp1, wp2)
        - Input: Two Waypoints
        - Output: A number.
        Description: Calculates Haversine distance between the two points.


    Flightplan:

        FlighPlan Class
        - Route (vector of Waypoint, will follow in order, one way)
        - Total route distance (number)

        FlightPlan()
        - Input: None.
        - Output: Empty FlightPlan class object
        Description: Constructor.

        SetDeparture(fp, wp)
        - Input: One FlightPlan and one Waypoint.
        - Output: Number
        Description: Updates empty Flighplan with wp as it's first route element. Returns 0 if it was empty and -N if it had N elements.

        AddWaypoint(fp, wp)
        - Input: One FlightPlan and one Waypoint.
        - Output: Number
        Description: Updates a non-empty FlightPlan with a new Waypoint at the end of the current list. Returns -1 if it Fp was empty or 0 otherwise.

        ShowFlightPlan(fp)
        - Input: Flightplan
        - Output None
        Description: Shows on the scren the information of the list. It should use ShowWaypoint()
    
        "ADV":

        FinishFlightPlan(fp)
        - Input: Flightplan
        - Output Number
        Description: Sets attribute total route distance of the flight plan. Use CalculateDistance. Returns -1 if fp was empty or the distance otherwise.

        SearchWaypointByName(fp, name)
        - Input: Flightplan
        - Output Number
        Description: Loop over route of fp searching for a wp with input name. Returns position of the waypoint in the vector or -1 if not found.

        PlotFlightPlan(fp)
        - Input: Flightplan
        - Output Number
        Description: Shows a plot with the flight plan route. Assume cartesian coordinates. Returns -1 if fp was empty or the distance otherwise.

        LoadFlightPlan(filename, fp)
        - Input: Filename and empty flightplan.
        - Output None
        Description: Read flight plan route and create a new waypoint for every line with text. Returns -1 if filename does not exist of the number of waypoints if it does.

        IsPath(fp, name1, name2)
        - Input: Flightplan and 2 strings
        - Output Boolean
        Description: Checks if the fp has a path to connect wp with name1 with wp with name2. Use the SearchWaypointByName. Returns True if path exists and False if it's empty or route does not exist.

    Main program for Phase Zero:

    Will loop on these steps:
    - Informing the user about available functionalities
    - executing the selected option

    Available options, at least:

    1. Create WP and add to a NEW FP
    2. Create WP and add to EXISTING FP
    3. Finish FP and show distance
    4. Load FP from a file
    5. Show the FP
    6. Plot the FP
    7. Check if path exists in the FP
    0. End program


Phase One: The Graph.

Will build the data model for a NODE, SEGMENT and a GRAPH to store the points (nodes) and their connections (segments).

Functions: Plot and visualize the graph. 

Simple test program to load graph with a simple set of points and connections verifying the functions.

