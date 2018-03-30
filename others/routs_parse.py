import requests
import json

link = 'https://maps.googleapis.com/maps/api/directions/json?origin=Palasia%20Square,%2025,%20Mahatma%20Gandhi%20Rd,%20Old%20Palasiya,%20New%20Palasia,%20Indore,%20Madhya%20Pradesh%20452001&destination=Bhawarkuan%20Square%20Bus%20Stop,%20Khandwa%20Rd,%20Indrapuri%20Colony,%20Bhanwar%20Kuwa,%20Indore,%20Madhya%20Pradesh%20452001&key=AIzaSyBgf0BXB6S-mScrgNTzQWBDcDqYndpxq6M'
data = requests.get(link).text

data = json.loads(data)
# print(data['routes'][0]['legs'][0]['steps'])

for i in data['routes'][0]['legs'][0]['steps']:
    lattitude = i['start_location']['lat']
    longitude = i['start_location']['lng']
    print('{}, {}'.format(lattitude, longitude))
