# Project Statement

## Problem Statement
Preparing a flight plan by hand is slow and can have mistakes. Distance, flight time and fuel must be worked out for every route and aircraft. Beginners also find it hard to see how these values are calculated.

The aim of this project is to build a simple Python program that takes basic flight details from the user and creates a clear flight plan automatically.

## Scope of the Project
- Works with 8 fixed airports: Delhi, Mumbai, Bengaluru, Chennai, Hyderabad, Kolkata, Dubai and London.
- Works with 3 aircraft types: Boeing 737, Airbus A320 and Boeing 777.
- Calculates distance, flight time, arrival time, trip fuel, reserve fuel and total fuel.
- Creates 3 waypoints between the two airports.
- Shows stored weather data for both airports. The weather is not live.
- Runs in the terminal. It does not use a database or the internet.
- The plan is an educational estimate. It is not for real flight operations.

## Target Users
- Students learning Python.
- Teachers who need a simple example project.
- Beginners interested in aviation.

## High-Level Features
1. Airport selection with a numbered menu.
2. Aircraft selection showing speed and fuel burn.
3. Passenger count input with checks.
4. Distance calculation using the Haversine formula.
5. Flight time, arrival time and fuel calculation (10% reserve fuel).
6. Route waypoints with coordinates.
7. Weather details for departure and destination.
8. Error handling for wrong input and for the same departure and destination.
9. Code divided into six modules (data, calculations, route, input, display and main).
