# Digital Flight Plan Generator

## Overview
A simple Python program that creates a digital flight plan. The user selects a departure airport, a destination airport, an aircraft and the number of passengers. The program then shows the distance, flight time, fuel needed, weather and route.

This project was made for the course **Python Essentials** at VIT Bhopal University.

## Features
- Numbered menus for airports and aircraft
- Input checks for wrong or empty input
- Distance calculation using the Haversine formula
- Flight time, arrival time and fuel calculation with 10% reserve fuel
- Three route waypoints with coordinates
- Weather details for both airports
- Code divided into six modules

## Technologies Used
- Python 3
- Built-in modules only: `math`, `random`, `datetime`

## Project Structure
```
Flight-Plan-Generator/
  main.py             menu and program flow (run this file)
  data.py             airports, weather and aircraft data
  calculations.py     calculate_distance, convert_time
  route.py            generate_waypoints
  input_handler.py    choose_airport, choose_aircraft, get_passengers
  display.py          print_header, display_airports, generate_flight_plan
  README.md
  statement.md
```

| File | Purpose |
|------|---------|
| main.py | Shows the main menu and controls the program |
| data.py | Stores the `airports`, `weather` and `aircraft` dictionaries |
| calculations.py | Distance (Haversine formula) and time conversion |
| route.py | Creates three waypoints between two airports |
| input_handler.py | Reads and checks the user's choices |
| display.py | Prints menus, calculates fuel and time, and prints the flight plan |

## How to Install and Run
1. Install Python 3 from https://www.python.org/downloads/
2. Download or clone the project:
   ```
   git clone https://github.com/aaryan26bmr10023/Flight-Plan-Generator.git
   cd Flight-Plan-Generator
   ```
3. Run the program:
   ```
   python main.py
   ```
4. Choose option 1, then select the airports, aircraft and passengers.

No extra packages need to be installed. All six `.py` files must be in the same folder.

## How to Test
Run `python main.py` and try these cases:

| Test | Input | Expected result |
|------|-------|-----------------|
| Valid flight | Delhi, Mumbai, Airbus A320, 150 | Distance 1137.05 km, time 1 h 22 m |
| Same airports | Same destination as departure | Error message, asks again |
| Text instead of number | `abc` | "Please enter a number" message |
| Choice out of range | `99` | "Invalid choice" message |
| Negative passengers | `-5` | "Cannot be negative" message |
| Wrong menu option | `7` | "Please enter 1 or 2" message |
| Exit | `2` | Thank-you message and program ends |

## Sample Output
Delhi to Mumbai, Airbus A320, 150 passengers:
```
Distance            : 1137.05 km
Estimated Time      : 1 hours 22 minutes
Trip Fuel           : 3425 L
Reserve Fuel        : 342 L
Total Fuel Required : 3767 L
```

## Note
This is an educational project. Weather data is fixed sample data. The flight plan must not be used for real flying.

## Author
Aaryan Sharma (26BMR10023) - VIT Bhopal University
