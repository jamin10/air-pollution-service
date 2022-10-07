from client_cities import *

class Service:

    def __init__(self, client_cities, client_pollution, repository_client):
        self.client_cities = client_cities
        self.client_pollution = client_pollution
        self.repository_client = repository_client

    def run(self, params):
        cities_data = self.client_cities.get_cities_data(params)
        print(cities_data)

        pollution_data = []
        for city in cities_data:
            pollution = self.client_pollution.get_pollution_data(city)
            pollution_data.append(pollution)

        print(pollution_data)

        self.repository_client.create_tables()

        for city, pollution in zip(cities_data, pollution_data):
            self.repository_client.insert_data(city, pollution)
