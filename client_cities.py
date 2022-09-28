from dataclasses import dataclass
import requests

# Add documentation
# Add a link to the website which specifies this link: <www.hello.com> 
URL_GET_CITIES = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

class CitiesClient: 

    def _init_(self, API_key):
        self.API_key = API_key

    def headers(self) -> dict:
        return {
            "X-RapidAPI-Key": self.API_key,
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }

    def execute(self, method: str, url: str, params: dict):
        return requests.request(method, url, self.headers, params).json()
    

    def get_cities_data(self, min_population: int):
        # We are using these params because... (less verbose)

        # Todo: Move to @dataclass GetCitiesParams for cleanness
        params = {"minPopulation":  min_population}

        # Execute GET request
        response = self.execute("GET", URL_GET_CITIES, self.headers, params)

        # Todo: Map the request.Response to custom data Class
        cities = []
        for city_data in response["data"]:
            
            # Todo: Raise KeyError exception if expected keys are not present
            city = City(
                city_data["id"],
                city_data['name'],
                city_data['latitude'],
                city_data['longitude'],
                city_data['population']
            )

            cities.append(city)

        return cities

@dataclass
class GetCitiesParams:
    min_population: int

@dataclass
class City:
    id: str
    name: str
    latitude: str
    longitude: str
    population: str