import googlemaps


# Replace the API key below with a valid API key.
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

# Geocoding and address
geocode_result = gmaps.geocode('Rua Silva Barros, 107, Sorocaba, SP')
print("geocode_result = ", geocode_result)

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
#
# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
