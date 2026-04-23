import requests
import json

API_KEY = "4189bb85377ac60369009c5b1985c11a"
location = input("Enter location (London,Paris,Tokyo,Mumbai) to know weather report:")
# weather_url = "http://api.weatherstack.com/current?access_key=YOUR_API_KEY&query=London"
server_url  = "http://api.weatherstack.com/current"
query_url = f"?access_key={API_KEY}&query={location}"
weather_url = server_url + query_url
response = requests.get(weather_url)
#print(dir(response))
data = response.json()
def weather_data():

    print(f"{data['request']['query']}")
    print(f"""
            -------WEATHER REPORT--------
            location :  {data['location']['name']}
            lat - lon :  {data['location']['lat']} -{data['location']['lon']}   
            localtime:   {data['location']['localtime']}
            observation_time :  {data['current']['observation_time']}
            temp:   {data['current']['temperature']}
            weather_descriptions:  {data['current']['weather_descriptions'][0]}
            sunrise -sunset: {data['current']['astro']['sunrise']} - {data['current']['astro']['sunset']}
            """)
store_data = {
     
            "location" :  data['location']['name'],
            "lat" : data['location']['lat'], 
            "lon" : data['location']['lon'],  
            "localtime" :  data['location']['localtime'],
            "observation_time" :  data['current']['observation_time'],
            "temp"    :   data['current']['temperature'],
            "weather_descriptions":  data['current']['weather_descriptions'][0],
            "sunrise" : data['current']['astro']['sunrise'],
            "sunset"  :   data['current']['astro']['sunset'],
            
}    
weather_data()

with open("outputweather.json", "w") as file:
    json.dump(store_data, file, indent=4)