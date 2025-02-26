import requests
from datetime import datetime


MY_LAT = 36.305804
MY_LONG = 59.516963

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)


parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
print(sunset, sunrise)

time_now = datetime.now()
print(time_now.hour)
