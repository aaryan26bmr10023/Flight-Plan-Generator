from display import print_header,generate_flight_plan
from input_handler import choose_airport,choose_aircraft,get_passengers

# MAIN PROGRAM
def main():
    while True:
        print_header()
        print("\n1. Generate Flight Plan")
        print("2. Exit")
        choice=input("\nEnter your choice: ").strip()
        if choice=="1":
            print("\n"+"="*85)
            print("                         FLIGHT INFORMATION")
            print("="*85)
            departure_name=choose_airport("Select departure airport")
            while True:
                destination_name=choose_airport("Select destination airport")
                if departure_name==destination_name:
                    print(
                        "\nERROR: Departure and destination cannot be the same."
                    )
                    print("Please select another destination.\n")
                    continue
                break
            aircraft_name=choose_aircraft()
            passengers=get_passengers()
            generate_flight_plan(
                departure_name,
                destination_name,
                aircraft_name,
                passengers
            )
            while True:
                again=input(
                    "\nEnter 1 to create a new flight, or 2 to exit: "
                ).strip()
                if again=="1":
                    break
                if again=="2":
                    print("\nThank you for using the Flight Plan Generator.")
                    return
                print("Invalid choice. Please enter 1 or 2.")
        elif choice=="2":
            print("\nThank you for using the Flight Plan Generator.")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

# START PROGRAM
if __name__=="__main__":
    main()
