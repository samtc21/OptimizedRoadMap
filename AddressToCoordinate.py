import googlemaps

def AddressToCoordinates( address):

    # Define the Google Maps API key
    gmaps = googlemaps.Client(key='AIzaSyBJo-WJPJy2F76JzDcUvBXUErAaLs9oMGM')

    # Use the Google Maps API to convert the address into coordinates
    geocode_result = gmaps.geocode(address)

    # Extract the latitude and longitude from the geocode result
    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']
    coordinates = (latitude, longitude)
    return coordinates
