from curses import curs_set
from config import load_config
import psycopg2

class PostgreSqlRepository:

    def __init__(self, config):
        self.hostname = config.host
        self.database = config.db_name
        self.username = config.db_username
        self.password = config.db_password
        self.port_id = config.port_id

    def get_connection_variables(self) -> str:
        connection_variables = f"host={self.hostname} dbname={self.database} user={self.username} \
                                    password={self.password} port={self.port_id}"
        return connection_variables

    def create_tables(self):
        conn = None
        # Create connection to database
        try: 
            with psycopg2.connect(
                self.get_connection_variables()
                ) as conn: 

                with conn.cursor() as cur:

                    create_cities = ''' CREATE TABLE IF NOT EXISTS cities (
                                            id  integer PRIMARY KEY,
                                            name  varchar(50), 
                                            lat  numeric, 
                                            long  numeric,
                                            population integer
                                            ) '''
                    cur.execute(create_cities)

                    create_pollution = ''' CREATE TABLE IF NOT EXISTS pollution (
                                                id SERIAL PRIMARY KEY,
                                                city_id  integer REFERENCES cities(id),
                                                datetime  numeric,
                                                aqi  integer
                                                ) '''
                    cur.execute(create_pollution)

                    create_components = ''' CREATE TABLE IF NOT EXISTS components (
                                                id integer PRIMARY KEY REFERENCES pollution(id) UNIQUE,
                                                co  numeric,
                                                no numeric,
                                                no2 numeric,
                                                o3 numeric,
                                                so2 numeric,
                                                pm2_5 numeric, 
                                                pm10 numeric, 
                                                nh3 numeric
                                                ) '''
                    cur.execute(create_components)

        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        
    def insert_data(self, city, pollution):
        
        conn = None
        try:
            with psycopg2.connect(
                self.get_connection_variables()
                ) as conn: 

                with conn.cursor() as cur:

                    insert_cities = ''' INSERT INTO cities (id, name, lat, long, population) VALUES (%s, %s, %s, %s, %s) '''
                    insert_cities_values = (city.id, city.name, city.latitude, city.longitude, city.population)
                    cur.execute(insert_cities, insert_cities_values)

                    insert_pollution = ''' INSERT INTO pollution (city_id, datetime, aqi) VALUES (%s, %s, %s) RETURNING id'''
                    insert_pollution_values = (city.id, pollution.dt, pollution.aqi)
                    cur.execute(insert_pollution, insert_pollution_values)
                    id_new_row = cur.fetchone()[0]

                    insert_components = ''' INSERT INTO components (id, co, no, no2, o3, so2, pm2_5, pm10, nh3) 
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id'''
                    insert_components_values = (id_new_row, pollution.co, pollution.no, pollution.no2, pollution.o3, \
                                                    pollution.so2, pollution.pm2_5, pollution.pm10, pollution.nh3 )
                    cur.execute(insert_components, insert_components_values)

                conn.commit()

        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()



# test = PostgreSqlRepository(load_config())
# test.create_tables()
# test.insert_data()