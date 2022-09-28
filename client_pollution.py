import requests

class Pollution:

    def __init__(self, API_key):
        self.API_key = API_key


    def get_pollution_data(self, latitude, longitude):

        url2 = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={self.API_key}"

        response_OW = requests.get(url2)
        response_OW = response_OW.json()

        pollution_data = {}

        pollution_data['dt'] = response_OW['list'][0]['dt']
        pollution_data['aqi'] = response_OW['list'][0]['main']['aqi']
        pollution_data['components'] = response_OW['list'][0]['components']

        return pollution_data
