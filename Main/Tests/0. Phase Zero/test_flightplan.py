
from _0_PhaseZero import flightplan as fp
from _0_PhaseZero import waypoint as wp 

# create flightplan and show the content 
# of waypoint ist in the console

Waypoint1 = wp.WaypointClass("", "", "")
Waypoint2 = wp.WaypointClass("", "", "")

wp.LocateWaypoint(Waypoint1, 140, 200)
wp.NameWaypoint(Waypoint1, "Test Waypoint 1")

wp.LocateWaypoint(Waypoint2, 400, 600)
wp.NameWaypoint(Waypoint2, "Test Waypoint 2")


FlighPlanTest = fp.FlightPlanClass([], "")

fp.SetFpDeparture(FlighPlanTest, Waypoint1)
fp.AddWaypointToFp(FlighPlanTest, Waypoint2)

fp.ShowFlightPlan(FlighPlanTest)    

print(fp.FinishFlightPlan(FlighPlanTest))
fp.PlotFlightPlan(FlighPlanTest)
