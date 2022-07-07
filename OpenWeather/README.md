# Openweather
![python](https://img.shields.io/badge/Python-blueviolet?style=plastic&logo=python&logoColor=FFD43B)

Openweather is an online service that allows you to access a multitude of weather data both through its website and through its API.

This service has various payment options that allow you to access a greater amount of data and continuously, however, it has a free API with more than enough data for this topic.

## Registrarse
In order to make use of this API it is necessary to register in [openweathermap](https://openweathermap.org/), choose the free plan (Obviously, you can pay for any other plan and access much more data) and obtain an API key to be able to make requests.

## Proccess
Geting the data with python is very simple since the API offers the information in json format. 
To see in a simple way how the data is distributed, we can access the information on the website (https://openweathermap.org/current)

For example to access the temperature value:
```python
response = requests.get(url)
data = json.loads(response.text)
weather=data['weather'][0]['main']

```

## Results
The result for Paris with the data, we are interested in, would be as follows:

| City   | Temp. (ºC)   | Description   | Sunrise - Sunset    | Wind Speed   | Clouds   | Humidity   | T.Max - T.Min   | Measurement Time   |
|--------|--------------|---------------|---------------------|--------------|----------|------------|-----------------|--------------------|
| Paris  | 18.86 ºC     | broken clouds | 03:55:17 - 19:55:18 | 4.02 km/h    | 79 %     | 72 %       | 19.58 - 16.26   | 23:01:00           |

