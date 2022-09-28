import requests

class Cities: 

    def _init_(self, API_key):
        self.API_key = API_key

    def get_cities_data(self):
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

        querystring = {"minPopulation":"400000"}

        headers = {
            "X-RapidAPI-Key": self.API_key,
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }

        response_GeoDB = requests.request("GET", url, headers=headers, params=querystring)
        response_GeoDB = response_GeoDB.json()

        data_GeoDB = response_GeoDB['data']

        cities_data = []

        for data in data_GeoDB:
            city_data = {}

            city_data['id'] = data['id']
            city_data['name'] = data['name']
            city_data['latitude'] = data['latitude']
            city_data['longitude'] = data['longitude']
            city_data['population'] = data['population']

            cities_data.append(city_data)

        return cities_data