# WEB SCRAPING
![python](https://img.shields.io/badge/Python-blueviolet?style=plastic&logo=python&logoColor=FFD43B)

The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser. It is a form of copying in which specific data is gathered and copied from the web.

The [weather.com](https://weather.com/) website has been used for this example.

## Data required
There are two sections in the code that need mentioning[^note].

#### 1. User Agent:
According to Wikipedia: 
> In computing, a user agent is any software, acting on behalf of a user, which "retrieves, renders and facilitates end-user interaction with Web content"

When a user accesses a web page, the application generally sends a text string that identifies the user agent to the server. The user agent ID is one of the exclusion criteria used by the robot exclusion standard to prevent access to certain sections of a website.

You can check your User agent [here](https://www.whatismybrowser.com/es/detect/what-is-my-user-agent/).

#### 2. Latitude and Longitude:
Weather.com allows access to its data with a latitude and longitude request, which is interesting and also allows access to very specific areas of the map.
Therefore, an intermediate step has been introduced at the beginning of the programme as follows:
```python
        url_ll.append(f'https://nominatim.openstreetmap.org/search/{city[i]}?format=json')
        r.append(requests.get(url_ll[i]))

        datos_r=r[i].json()

        lat.append(datos_r[0]['lat'])
        lon.append(datos_r[0]['lon'])
        
```

If you want you can directly attach a longitude and a latitude in the variables `lat` y `lon`.

The API used to get these data is [nominatim.openstreetmap.org](https://nominatim.openstreetmap.org/), in addition more data can be accessed if needed. Info on the output json format [here](https://nominatim.org/release-docs/develop/api/Search/).

**Et voilà**, we already have everything to make the request.

## Results

In this case the results have been printed for several cities around the world.

| City              | Temperature   | Description   | Sunrise - Sunset   | Wind Speed   | Humidity   | UV Index   | Measurement Time   |
|-------------------|---------------|---------------|--------------------|--------------|------------|------------|--------------------|
| Paris             | 18.89 ºC      | Clear         | 5:55 am - 9:55 pm  | 11.26 km/h   | 67%        | 0 of 10    | 1:19 am CEST       |
| Madrid            | 20.56 ºC      | Clear         | 6:51 am - 9:47 pm  | 16.09 km/h   | 59%        | 0 of 10    | 1:18 am CEST       |
| Los Ángeles       | 25.0 ºC       | Sunny         | 5:47 am - 8:07 pm  | 12.87 km/h   | 54%        | 5 of 10    | 4:14 pm PDT        |
| Yellowknife       | 23.89 ºC      | Sunny         | 3:56 am - 11:27 pm | 16.09 km/h   | 36%        | 3 of 10    | 5:18 pm MDT        |
| Oslo              | 12.78 ºC      | Rain          | 4:07 am - 10:35 pm | 12.87 km/h   | 91%        | 0 of 10    | 1:25 am CEST       |
| Tokyo             | 26.11 ºC      | Mostly Cloudy | 4:31 am - 7:00 pm  | 14.48 km/h   | 75%        | 4 of 10    | 8:21 am JST        |
| Bangkok           | 27.78 ºC      | Fair          | 5:55 am - 6:50 pm  | 14.48 km/h   | 76%        | 0 of 10    | 6:23 am ICT        |
| Nueva Delhi       | 31.67 ºC      | Haze          | 5:29 am - 7:22 pm  | 11.26 km/h   | 71%        | 0 of 10    | 4:54 am IST        |
| Medellín          | 22.78 ºC      | Partly Cloudy | 5:52 am - 6:21 pm  | 8.04 km/h    | 69%        | 0 of 10    | 6:18 pm COT        |
| Santiago de Chile | 7.22 ºC       | Mostly Cloudy | 7:47 am - 5:48 pm  | 12.87 km/h   | 79%        | 0 of 10    | 7:20 pm CLT        |
| Ciudad del Cabo   | 11.67 ºC      | Fair          | 7:51 am - 5:51 pm  | 14.48 km/h   | 81%        | 0 of 10    | 1:17 am SAST       |
| Jartum            | 31.67 ºC      | Mostly Cloudy | 5:24 am - 6:25 pm  | 11.26 km/h   | 43%        | 0 of 10    | 1:25 am CAT        |
| Antananarivo      | 11.11 ºC      | Fair          | 6:24 am - 5:25 pm  | 3.22 km/h    | 84%        | 0 of 10    | 2:28 am EAT        |
| Dubái             | 35.0 ºC       | Fair          | 5:34 am - 7:13 pm  | 20.92 km/h   | 52%        | 0 of 10    | 3:18 am GST        |
| Sidney            | 14.44 ºC      | Cloudy        | 7:00 am - 4:59 pm  | 19.31 km/h   | 87%        | 0 of 10    | 9:21 am AEST       |


#### Footer
[^note]: 
    In the code there are two variables to check the status of the HTTP response, for more information click [here](https://developer.mozilla.org/es/docs/Web/HTTP/Status).

    ```python
    http_code.append(res[i].status_code)
    http_code_reason.append(res[i].reason)

    ```

    In this way it can be determined whether the connection was successful or whether there was an error and what type of error it is, for example:

    A good connection return:
    `- http code, reason: 200, OK`

    A client error responses could be:
    `- http code, reason: 404, Not Found`


