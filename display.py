import random
from datetime import datetime,timedelta
from data import airports,weather,aircraft
from calculations import calculate_distance,convert_time
from route import generate_waypoints

# Terminal display functions
def print_header():
    print("\n"+"="*85)
    print("✈ INDIGO AIRLINES")
    print("DIGITAL FLIGHT PLAN")
    print("="*85)

def display_airports():
    print("\nAVAILABLE AIRPORTS")
    print("-"*50)
    airport_list=list(airports.keys())
    i=1
    for airport_name in airport_list:
        airport=airports[airport_name]
        print(
            i,".",airport_name,"-",airport["city"]
        )
        i=i+1
    print("-"*50)

# Generate flight plan
def generate_flight_plan(departure_name,destination_name,aircraft_name,passengers):
    if departure_name==destination_name:
        print("\nERROR: Departure and destination cannot be the same.")
        return
    departure=airports[departure_name]
    destination=airports[destination_name]
    waypoints=generate_waypoints(departure,destination)
    flight_number="6E-"+str(random.randint(100,999))
    selected_aircraft=aircraft[aircraft_name]
    speed=selected_aircraft["speed"]
    fuel_burn=selected_aircraft["fuel_burn"]
    distance=calculate_distance(
        departure["lat"],
        departure["lon"],
        destination["lat"],
        destination["lon"]
    )
    flight_time=distance/speed
    hours, minutes=convert_time(flight_time)
    departure_time=datetime.now()
    arrival_time=departure_time+timedelta(
        hours=hours,
        minutes=minutes
    )
    departure_time_text=departure_time.strftime("%H:%M")
    arrival_time_text=arrival_time.strftime("%H:%M")
    departure_weather=weather[departure["code"]]
    destination_weather=weather[destination["code"]]
    fuel_required=flight_time*fuel_burn
    reserve_fuel=fuel_required*0.10
    total_fuel=fuel_required+reserve_fuel

   # Display results
    print("\n\n")
    print("✈  INDIGO AIRLINES")
    print("DIGITAL FLIGHT PLAN")
    print("═"*85)
    print("\n  FLIGHT SUMMARY")
    print("-"*85)
    print("\n  FLIGHT NUMBER :",flight_number)
    print("\n  DEPARTURE              DESTINATION              ROUTE")
    print(" ",departure_name," "*(25-len(departure_name)),
    destination_name," "*(25-len(destination_name)),
    departure["code"],"→",destination["code"])
    print("\n  PASSENGERS              AIRCRAFT                 FLIGHT TIME")
    print(" ",passengers," "*(25-len(str(passengers))),
    aircraft_name," "*(25-len(aircraft_name)),
    hours, "h",minutes, "m")
    print("\n  Departure Time      :",departure_time_text)
    print("  Estimated Arrival   :",arrival_time_text)
    print("\n  AIRCRAFT & FUEL INFORMATION")
    print("-"*85)
    print("\n  Aircraft Type       :",aircraft_name)
    print("  Cruise Speed        :",speed, "km/h")
    print("  Fuel Burn Rate      :",fuel_burn, "L/hour")
    print("  Trip Fuel           :",round(fuel_required), "L")
    print("  Reserve Fuel        :",round(reserve_fuel), "L")
    print("  Total Fuel Required :",round(total_fuel), "L")
    print("\n  WEATHER CONDITIONS")
    print("-"*85)
    print("\n  DEPARTURE -",departure["code"])
    print("  Condition           :",departure_weather["condition"])
    print("  Temperature         :",departure_weather["temperature"],"°C")
    print("  Wind Speed          :",departure_weather["wind"],"km/h")
    print("  Visibility          :",departure_weather["visibility"],"km")
    print("\n  DESTINATION -",destination["code"])
    print("  Condition           :",destination_weather["condition"])
    print("  Temperature         :",destination_weather["temperature"],"°C")
    print("  Wind Speed          :",destination_weather["wind"],"km/h")
    print("  Visibility          :",destination_weather["visibility"],"km")
    print("\n  ROUTE INFORMATION")
    print("-"*85)
    print("\n  ROUTE SEQUENCE\n")
    route=departure["code"]
    for waypoint in waypoints:
        route=route+"  →  "+waypoint["name"]
    route=route+"  →  "+destination["code"]
    print(" ",route)
    print("\n  WAYPOINT COORDINATES\n")
    print(
        "  1.",departure["code"],
        "LAT:",round(departure["lat"], 4),
        "LON:",round(departure["lon"], 4)
    )
    for i, waypoint in enumerate(waypoints,start=2):
        print(
            " ",i,".",waypoint["name"],
            "LAT:",round(waypoint["lat"],4),
            "LON:",round(waypoint["lon"],4)
        )
    print(
        " ",len(waypoints)+2,".",destination["code"],
        "LAT:",round(destination["lat"],4),
        "LON:",round(destination["lon"],4)
    )
    print("\n  Distance            :", round(distance, 2),"km")
    print("  Estimated Time      :", hours,"hours", minutes,"minutes")
    print("\n  FLIGHT STATUS")
    print("-"*85)
    print("\n  ✓ FLIGHT PLAN GENERATED SUCCESSFULLY")
    print("\n  This flight plan is an educational estimate.")
    print("  Fuel and flight-time values are calculated by this project.")
    print("\n"+"═"*85)
