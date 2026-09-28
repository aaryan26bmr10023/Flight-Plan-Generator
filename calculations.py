import math

# Distance calculations
def calculate_distance(lat1,lon1,lat2,lon2):
    R=6371
    difference_lat=math.radians(lat2-lat1)
    difference_lon=math.radians(lon2-lon1)
    lat1=math.radians(lat1)
    lat2=math.radians(lat2)
    # Haversine formula
    a=(
        math.sin(difference_lat/2)**2
        +math.cos(lat1)
        *math.cos(lat2)
        *math.sin(difference_lon/2)**2
    )
    c=2*math.atan2(math.sqrt(a),math.sqrt(1 - a))
    distance=R*c
    return distance
def convert_time(hours):
    whole_hours=int(hours)
    minutes=int((hours-whole_hours)*60)
    return whole_hours,minutes
