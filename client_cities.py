from dataclasses import dataclass, asdict
import requests
from config import *

# Add documentation
# Add a link to the website which specifies this link: <www.hello.com> 
URL_GET_CITIES = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

class CitiesClient: 

    def __init__(self, config):
        self.api_key_geodb = config.api_key_geodb

    def headers(self) -> dict:
        return {
            "X-RapidAPI-Key": self.api_key_geodb,
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }

    def execute(self, method: str, url: str, headers: dict, params: dict):
        return requests.request(method, url, headers=headers, params=params).json()
    
    def get_cities_data(self, params):
        # Execute GET request
        response = self.execute("GET", URL_GET_CITIES, self.headers(), asdict(params))

        # Map the request.Response to custom data Class
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
    location: str = None # Only cities near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    limit: str = None # The maximum number of results to retrieve
    countryIds: str = None # Only cities in these countries (comma-delimited country codes or WikiData ids)
    minPopulation: str = None # Only cities having at least this population
    maxPopulation: str = None # Only cities having no more than this population
    namePrefix: str = None # Only cities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.
    radius: str = None # The location radius within which to find cities
    distanceUnit: str = None # The unit of distance to use: MI | KM
    offset: str = None # The zero-ary offset into the results
    excludedCountryIds: str = None # Only cities NOT in these countries (comma-delimited country codes or WikiData ids)
    sort: str = None # How to sort the results. Format: ±SORTFIELD,±SORTFIELD where SORT_FIELD = countryCode | elevation | name | population
    timeZoneIds: str = None # Only cities in these time-zones
    asciiMode: str = None # Display results using ASCII characters
    languageCode: str = None # Display results in this language
    types: str = None # Only cities for these types (comma-delimited): CITY | ADM2

@dataclass
class City:
    id: str
    name: str
    latitude: str
    longitude: str
    population: str


############################################
api_key = 'b29f2328d6mshfe5d6639483b6a2p166f69jsn5c93c74e7d77'
test = CitiesClient(load_config())
params = GetCitiesParams(minPopulation='200000', offset='100')
data = test.get_cities_data(params)
print(data)