from curses import curs_set
import psycopg2

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
password = 'postgres'
port_id = 5432

class PostgreSqlRepository:

    def __init__(self, hostname: str, database: str, username: str, password: str, port_id: int):
        self.hostname = hostname
        self.database = database
        self.username = username
        self.password = password
        self.port_id = port_id

    def create_tables(self):

        conn = None
        # Create connection to database
        try: 
            with psycopg2.connect(
                host = self.hostname,
                dbname = self.database,
                user = self.username, 
                password = self.password,
                port = self.port_id
                ) as conn: 

                with conn.cursor() as cur:

                    create_cities = ''' CREATE TABLE IF NOT EXISTS cities (
                                            id  integer PRIMARY KEY,
                                            name  varchar(50), 
                                            lat  numeric, 
                                            long  numeric,
                                            population  integer
                                            ) '''
                    cur.execute(create_cities)

                    create_pollution = ''' CREATE TABLE IF NOT EXISTS pollution (
                                                id  integer PRIMARY KEY,
                                                city_id  integer REFERENCES cities(id),
                                                datetime  numeric,
                                                aqi  integer 
                                                ) '''
                    cur.execute(create_pollution)

                    create_components = ''' CREATE TABLE IF NOT EXISTS components (
                                                pollution_id  integer REFERENCES pollution(id) UNIQUE,
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
        
    def insert_data(self):
        pass


test = PostgreSqlRepository(hostname, database, username, password, port_id)
test.create_tables()