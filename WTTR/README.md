# WTTR


wttr.in is a free service that is under development but has gained a lot of relevance. We are going to see how to get data from this service, since, apart from getting them directly from the web, we can work with them and print them on the console.

## Formats
If we look at the official [wttr.in documentation](https://github.com/chubin/wttr.in) we see that we can get the output data in different formats, here is an example of some of them, obtained by running the wttr_2 file:

**Format 1:** ☀️   +21°C

**Format 2:** ☀️   🌡️+21°C 🌬️↘9km/h

**Format 3:** paris: ☀️   +21°C

**Format 4:** paris: ☀️   🌡️+21°C 🌬️↘9km/h

**Custom Format:** paris: ☀️   +21°C

**Custom Format 2:** paris: ☀️   +21°C ,Wind: ↘9km/h Humidity: 60% Local_Timezone: Europe/Paris 00:05:10+0200 Precipitation: 0.0mm Moon Phase: 🌓

Special mention for the following format with graphics included.

**Format v2:**

<img width="419" alt="image" src="https://user-images.githubusercontent.com/107102754/177652566-6d39cbb5-f1b8-4d01-8fb2-83f4cdd03f43.png">

<img width="415" alt="image" src="https://user-images.githubusercontent.com/107102754/177652649-8380738a-797a-4737-90bf-582e011c63ca.png">

However, we will work with the json format.

To visualise how to access each data click [here](https://wttr.in/nemours?format=j1). This makes it easier to know which index the data correspond to.

For example, to get the temperature in Celsius:
```python
url = f'https://wttr.in/{place}?format=j1'

res = requests.get(url)
json_format = res.json()

temp=json_format["current_condition"][0]['temp_C']

```

## Language
In addition, the information can be obtained in another language, for example for Spanish it would be:

`url=f'https://es.wttr.in/{place}'`

## Results

When you run the code you get:

| Place   | Temp. (ºC)   | Description   | Sunrise - Sunset    | Wind Speed   | Humidity   | UV Index   | Measurement Time   |
|---------|--------------|---------------|---------------------|--------------|------------|------------|--------------------|
| Paris   | 21 ºC        | Clear         | 05:55 AM - 09:56 PM | 9 km/h       | 60 %       | 6/10       | 08:56 PM           |

This is just an example to visualize the data, however, we can use each of the isolated data for different functions.
