# Generate waypoints
def generate_waypoints(departure,destination):
    waypoints=[]
    number_of_waypoints=3
    for i in range(1,number_of_waypoints+1):
        fraction=i/(number_of_waypoints+1)
        latitude=(
            departure["lat"]
            +(destination["lat"]-departure["lat"])*fraction
        )
        longitude=(
            departure["lon"]
            +(destination["lon"]-departure["lon"])*fraction
        )
        waypoint={
            "name":"WPT-"+departure["code"]+str(i),
            "lat":latitude,
            "lon":longitude
        }
        waypoints.append(waypoint)
    return waypoints
