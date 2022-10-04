from dataclasses import dataclass
import requests
from config import *

# Open Weather air pollution API documentation 
# https://openweathermap.org/api/air-pollution

class PollutionClient:

    def __init__(self, config):
        self.API_key = config.api_key_open_weather

    def get_pollution_data(self, city):
        latitude = city.latitude 
        longitude = city.latitude

        URL_OPEN_WEATHER_POLLUTION = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={self.API_key}"

        response_OW = requests.get(URL_OPEN_WEATHER_POLLUTION)
        response_OW = response_OW.json()

        pollution = Pollution(
                        latitude,
                        longitude,
                        response_OW['list'][0]['dt'],
                        response_OW['list'][0]['main']['aqi'],
                        response_OW['list'][0]['components']['co'],
                        response_OW['list'][0]['components']['no'],
                        response_OW['list'][0]['components']['no2'],
                        response_OW['list'][0]['components']['o3'],
                        response_OW['list'][0]['components']['so2'],
                        response_OW['list'][0]['components']['pm2_5'],
                        response_OW['list'][0]['components']['pm10'],
                        response_OW['list'][0]['components']['nh3'])

        return pollution

@dataclass
class Pollution:
    lat: float
    long: float
    dt: int
    aqi: int
    co: float
    no: float
    no2: float
    o3: float
    so2: float
    pm2_5: float
    pm10: float
    nh3: float

# test = PollutionClient(load_config())
# data = test.get_pollution_data()
# # print(data)