# Air Pollution Service

This service combines data for cities and air pollution at a specific coordinate from two public APIs. This data is then persisted into a database. 

## APIs 
#### GeoDB Cities
* Data for cities is accessed through GeoDB Cities API
* Criteria can be specified through search parameter and a list of matching cities is returned
* Register for an account for API Key \
http://geodb-cities-api.wirefreethought.com/

#### Open Weather
* Data for air pollution is accessed through Open Weather API
* Latitude and longitude values are used to get air pollution details for a certain city
* Register for an account for API Key \
https://openweathermap.org/api/air-pollution

## Usage
* Sign up for API Key access 
* Create `.env` file with API keys
* Change parameters in `main.py` 
* run `main.py`

## TODO:
* Connect to repository and persist data
* Set up service in docker 
* User Dockerfile for environment variables 
* Create API to access data