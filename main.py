from asyncore import poll
from nturl2path import url2pathname
from client_pollution import *
from client_cities import *
from repository import *
from service import Service 
import requests

from config import load_config

def set_city_parameters():
    # Set parameters to specify city details
    params = GetCitiesParams(
                location = None, # Only cities near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
                limit = None, # The maximum number of results to retrieve
                countryIds = None, # Only cities in these countries (comma-delimited country codes or WikiData ids)
                minPopulation = 50000, # Only cities having at least this population
                maxPopulation = None, # Only cities having no more than this population
                namePrefix = None, # Only cities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.
                radius = None, # The location radius within which to find cities
                distanceUnit = None, # The unit of distance to use: MI | KM
                offset = 15, # The zero-ary offset into the results
                excludedCountryIds = None, # Only cities NOT in these countries (comma-delimited country codes or WikiData ids)
                sort = None, # How to sort the results. Format: ±SORTFIELD,±SORTFIELD where SORT_FIELD = countryCode | elevation | name | population
                timeZoneIds = None, # Only cities in these time-zones
                asciiMode = None, # Display results using ASCII characters
                languageCode = None, # Display results in this language
                types = None # Only cities for these types (comma-delimited): CITY | ADM2
    )
    return params

if __name__ == '__main__':
    # Load config
    config = load_config()
    # Build clients
    cities_client = CitiesClient(config)
    pollution_client = PollutionClient(config)
    respository_client = PostgreSqlRepository(config)
    service = Service(cities_client, pollution_client, respository_client)

    # Run service
    service.run(set_city_parameters())