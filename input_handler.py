from data import aircraft, airports
from display import display_airports

def choose_airport(message):
    airport_list=list(airports.keys())
    while True:
        display_airports()
        try:
            choice=int(input(message+" (enter number): "))
            if 1<=choice<=len(airport_list):
                return airport_list[choice-1]
            print("Invalid choice. Please enter a valid airport number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def choose_aircraft():
    aircraft_list=list(aircraft.keys())
    print("\nAVAILABLE AIRCRAFT")
    print("-"*50)
    i=1
    for aircraft_name in aircraft_list:
        data=aircraft[aircraft_name]
        print(i,".",aircraft_name,"(Speed:",data["speed"],"km/h,","Fuel burn:",data["fuel_burn"],"L/hour)")
        i=i+1
    print("-"*50)
    while True:
        try:
            choice=int(input("Select aircraft (enter number): "))
            if 1<=choice<=len(aircraft_list):
                return aircraft_list[choice-1]
            print("Invalid choice. Please enter a valid aircraft number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def get_passengers():
    while True:
        try:
            passengers=int(input("Enter total passengers: "))
            if passengers<0:
                print("Number of passengers cannot be negative.")
                continue
            return passengers
        except ValueError:
            print("Please enter a valid whole number.")