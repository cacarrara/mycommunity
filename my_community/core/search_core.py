import googlemaps


def get_lat_lon(address)
    # Replace the API key below with a valid API key.
    gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

    geocode_result = gmaps.geocode(address)

    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    return (lat, lon)
