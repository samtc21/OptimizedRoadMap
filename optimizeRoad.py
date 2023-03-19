import googlemaps
from datetime import datetime
from pprint import pprint
from AddressToCoordinate import *


def optimizeRoad(list_of_addresses, start, finish):

    # Define the Google Maps API key
    gmaps = googlemaps.Client(key='AIzaSyBJo-WJPJy2F76JzDcUvBXUErAaLs9oMGM')

    #convert addresses into coordinates
    coordinates = []
    for x in list_of_addresses:
        coordinates.append(AddressToCoordinates(x))
    start_coordinates = AddressToCoordinates(start)
    finish_coordinates = AddressToCoordinates(finish)

    # Define the list of coordinates including the start and finish coordinates
    all_coordinates = [start_coordinates] + coordinates + [finish_coordinates]

    # Use the Google Maps API to calculate the optimal road
    optimized_route = gmaps.directions(origin=start, destination=finish, waypoints=coordinates, optimize_waypoints=True)

    # Extract the order of the coordinates in the optimal road
    order = optimized_route[0]['waypoint_order']

    # Create a list of the coordinates in the optimal road
    optimal_coordinates = []
    optimal_coordinates.append(start_coordinates)
    for i in order:
        optimal_coordinates.append(all_coordinates[i+1])
    optimal_coordinates.append(finish_coordinates)

    optimal_road = []
    for coord in optimal_coordinates:
        geocode_result = gmaps.reverse_geocode(coord)

        # Extract the formatted address from the geocode result
        formatted_address = geocode_result[0]['formatted_address']
        optimal_road.append(formatted_address)
    # Print the optimal road
    return( optimal_road)
