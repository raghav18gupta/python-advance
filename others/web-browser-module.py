from geopy.geocoders import GoogleV3
import requests, json, time
import webbrowser


def locate_bus():
    # Getting the latitude and longitude of bus
    link_bus = 'https://api.thingspeak.com/channels/478427/fields/1.json?api_key=0BGHNMN1HRECL0QU&results=2&location=true'
    bus = requests.get(link_bus).text
    bus = json.loads(bus)

    device_id = int(bus['feeds'][0]['field1'])
    lati_bus = float(bus['feeds'][0]['latitude'])
    longi_bus = float(bus['feeds'][0]['longitude'])
    print(lati_bus)
    print(longi_bus)
    return [lati_bus, longi_bus]



whereisBus = locate_bus()


geocoder = GoogleV3()
location_list = geocoder.reverse(whereisBus)
location = location_list[0]
address = location.address
print(address)


open_link = f'https://www.google.com/maps/place/{whereisBus[0]},{whereisBus[1]}/data=!3m1!1e3'
print(open_link)
webbrowser.open(open_link)
