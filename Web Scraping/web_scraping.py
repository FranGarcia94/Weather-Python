#============================ WEB SCRAPING ============================#
#                                                                      #
#                    Get weather data from weathe.com                  #
#                           Using web scraping                         #
#                                                                      #
#======================================================================#

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


# Cities from which the data will be get
city = ['Paris', 'Madrid', 'Los Ángeles', 'Yellowknife', 'Oslo', 'Tokyo', 'Bangkok', 'Nueva Delhi', 'Medellín', 'Santiago de Chile', 'Ciudad del Cabo', 'Jartum', 'Antananarivo', 'Dubái', 'Sidney']


# Variables
url_ll=[]; lat=[]; lon=[]; url=[]; r=[]; res=[]; soup=[]; temperature=[]; zone=[]; hour=[]; sunrise_sunset=[]
sunrise=[]; sunset=[]; wind_speed=[]; humidity=[]; uv_index=[]; temp=[]; desc=[]; http_code=[]; http_code_reason=[]

data_2=[]

user = {'user-agent' : 'INSERT USER AGENT HERE'} # User-agent


# Requests

def wb():
    for i in range(len(city)):

        # Intermediate step to get latitude and longitude
        url_ll.append(f'https://nominatim.openstreetmap.org/search/{city[i]}?format=json')
        r.append(requests.get(url_ll[i]))

        datos_r=r[i].json()

        lat.append(datos_r[0]['lat'])
        lon.append(datos_r[0]['lon'])


        # Data from:
        url.append(f'https://weather.com/weather/today/l/{lat[i]},{lon[i]}?par=google')


        # We send the User agent to the request and enter a maximum connection time of 20 seconds.
        res.append(requests.get(url[i], headers=user, timeout=20))


        # The following variables indicate the status of the response, that is, if it went well or if there was a problem.
        http_code.append(res[i].status_code)
        http_code_reason.append(res[i].reason)

        # 'Soup' is initialized
        soup.append(BeautifulSoup(res[i].text, 'html.parser'))


        # Variables

        temperature.append(soup[i].find('span',class_='CurrentConditions--tempValue--3a50n'))
        temp.append(round((float(temperature[i].text[:-1])-32)*(5/9),2))

        zone.append(soup[i].find('h1','CurrentConditions--location--kyTeL').text)

        hour.append(soup[i].find('span','CurrentConditions--timestamp--23dfw').text.replace('As of ',''))

        sunrise_sunset.append(soup[i].find_all('p','SunriseSunset--dateValue--N2p5B'))

        sunrise.append(sunrise_sunset[i][0].text)

        sunset.append(sunrise_sunset[i][1].text)

        wind_speed.append(str(round(int(soup[i].find_all('span','Wind--windWrapper--3aqXJ')[0].text.replace('Wind Direction','').replace('mph',''))*1.609,2)) + ' km/h')

        humidity.append(soup[i].find_all('div','WeatherDetailsListItem--wxData--2s6HT')[2].text)

        uv_index.append(soup[i].find_all('div','WeatherDetailsListItem--wxData--2s6HT')[5].text)

        desc.append(soup[i].find('div','CurrentConditions--phraseValue--2Z18W').text)


        data_2.append([city[i], str(temp[i]) + ' ºC', desc[i], sunrise[i] + ' - ' + sunset[i], wind_speed[i], humidity[i], uv_index[i], hour[i]])


    # Print data_2 with a 'github' format.
    
    print(tabulate(data_2, headers = [ 'City', 'Temperature', 'Description', 'Sunrise - Sunset', 'Wind Speed', 'Humidity', 'UV Index', 'Measurement Time'],tablefmt="github"))

    print('\n')



if __name__ == '__main__':
    wb()

