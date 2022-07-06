#================================ WTTR ================================#
#                                                                      #
#                    Get weather data from wttr.in                     #
#                                                                      #
#======================================================================#

import requests
from tabulate import tabulate


# We have flexibility with how to put the place, for example: 'Paris', 'Eiffel Tower', 'los angeles, california'.
# As we can see, it is also possible to put famous monuments.

place = 'Paris' # Insert Place here


# Request

url = f'https://wttr.in/{place}?format=j1'

res = requests.get(url)
json_format = res.json()


# Variables

temp=json_format["current_condition"][0]['temp_C']                          # Temperature in Celsius

desc=json_format["current_condition"][0]['weatherDesc'][0]["value"]         # Weather description

hour_of_data=json_format["current_condition"][0]['observation_time']        # Requests time

hour_of_request=json_format["current_condition"][0]['localObsDateTime']     # Observation data time

sunrise=json_format["weather"][0]["astronomy"][0]['sunrise']                # Sunrise

sunset=json_format["weather"][0]["astronomy"][0]['sunset']                  # Sunset

wind_speed=json_format["current_condition"][0]["windspeedKmph"]             # Wind speed

humidity=json_format["current_condition"][0]["humidity"]                    # Humidity

uv_index=json_format["current_condition"][0]["uvIndex"]                     # UV Index (1-10)

datas=[]

datas.append([place, temp + ' ºC', desc, sunrise + ' - ' + sunset, wind_speed + ' km/h', humidity + ' %', uv_index + '/10', hour_of_data])

# Print datas with a 'github' format.
print(tabulate(datas, headers = [ 'Place', 'Temp. (ºC)', 'Description', 'Sunrise - Sunset', 'Wind Speed', 'Humidity', 'UV Index', 'Measurement Time'],tablefmt="github"))

