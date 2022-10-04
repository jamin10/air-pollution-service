from client_cities import *

class Service:

    def __init__(self, client_cities, client_pollution):
        self.client_cities = client_cities
        self.client_pollution = client_pollution
        # self.reposiotry = repository

    def run(self, params):
        cities_data = self.client_cities.get_cities_data(params)
        print(cities_data)

        pollution_data = []
        for city in cities_data:
            pollution = self.client_pollution.get_pollution_data(city)
            pollution_data.append(pollution)

        print(pollution_data)