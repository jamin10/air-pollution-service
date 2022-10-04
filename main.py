from asyncore import poll
from nturl2path import url2pathname
import requests

from config import load_config


if __name__ == '__main__':
    # Load config
    config = load_config()

 # build client 1
 # build client 2 

 # build repo 
    # environment_varaibles to get username / password 


# call service object 


























# '''

# class City:

#     def __init__(self, name, latitude, longitude, population):
#         self.name = name
#         self.latitude = latitude
#         self.longitude = longitude
#         self.popultion = population
#         self.pollution = {}

#     def add_pollution(self, pollution):
#         if type(pollution) is Pollution:
#             self.pollution['dt'] = pollution.dt
#             self.pollution['aqi'] = pollution.aqi
#             self.pollution['components'] = pollution.components
#         else:
#             print('Must be a Pollution object')


# class Pollution:

#     def __init__(self, dt, aqi, components):
#         self.dt = dt
#         self.aqi = aqi
#         self.components = components
        

# # GeoDB Cities API

# url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

# querystring = {"minPopulation":"400000"}

# headers = {
# 	"X-RapidAPI-Key": "b29f2328d6mshfe5d6639483b6a2p166f69jsn5c93c74e7d77",
# 	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
# }

# response_GeoDB = requests.request("GET", url, headers=headers, params=querystring)
# response_GeoDB = response_GeoDB.json()

# data_GeoDB = response_GeoDB['data']

# cities_data = []

# for data in data_GeoDB:
#     city_data = {}

#     city_data['name'] = data['name']
#     city_data['latitude'] = data['latitude']
#     city_data['longitude'] = data['longitude']
#     city_data['population'] = data['population']

#     cities_data.append(city_data)


# # OpenWeather API
# API_key = '371506301b2009441f3135528150fb96'

# combined_data = []

# for data in cities_data:
#     lat = data['latitude']
#     lon = data['longitude']

#     pollution_data = data

#     url2 = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}"

#     response_OW = requests.get(url2)
#     response_OW = response_OW.json()

#     pollution_data['dt'] = response_OW['list'][0]['dt']
#     pollution_data['aqi'] = response_OW['list'][0]['main']['aqi']
#     pollution_data['components'] = response_OW['list'][0]['components']

#     combined_data.append(pollution_data)

# print(combined_data)

# '''