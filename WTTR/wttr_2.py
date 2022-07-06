import requests

place='paris'


# URL Formats:

url_json=f'https://wttr.in/{place}?format=j1'

url_1=f'https://wttr.in/{place}?format=1'

url_2=f'https://wttr.in/{place}?format=2'

url_3=f'https://wttr.in/{place}?format=3'

url_4=f'https://wttr.in/{place}?format=4'

url_plot=f'https://wttr.in/{place}?format=v2'


# Custom Format

url_custom=f'https://wttr.in/paris?format=%l:+%c+%t'

url_custom_2=f'https://wttr.in/paris?format=%l:+%c+%t+,Wind:+%w+Humidity:+%h+Local_Timezone:+%Z+%T+Precipitation:+%p+Moon Phase:+%m'


# Results

res=requests.get(url_1)
print(f'Format 1: {res.text}')

res=requests.get(url_2)
print(f'Format 2: {res.text}')

res=requests.get(url_3)
print(f'Format 3: {res.text}')

res=requests.get(url_4)
print(f'Format 4: {res.text}')

res=requests.get(url_custom)
print(f'Custom Format: {res.text}\n')

res=requests.get(url_custom_2)
print(f'Custom Format 2: {res.text}\n')

# Format v2
res=requests.get(url_plot)
print(f'Format v2: {res.text}\n')

