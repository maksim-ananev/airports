from db_connector import DBConnector

class Controller_airports():
    def __init__(self):
        self.db = DBConnector()

    def filtred_airports(self, min_lat, max_lat, min_lon, max_lon):

        db_connection = self.db.connect_to_db()
        cursor = db_connection.cursor()
        cursor.execute(f'SELECT city, country, airport, latitude, longitude FROM airports WHERE '
                       f'latitude BETWEEN {min_lat} and {max_lat} and '
                       f'longitude BETWEEN {min_lon} and {max_lon}')
        return cursor.fetchall()

    def filtred_routes_by_cities(self, city_from, city_to):
        db_connection = self.db.connect_to_db()
        cursor = db_connection.cursor()
        cursor.execute(f'SELECT src_airport, dst_airport, airplane FROM routes WHERE src_airport in (SELECT iata FROM airports WHERE city = \'{city_from}\') AND dst_airport in (SELECT iata FROM airports WHERE city = \'{city_to}\')')
        return cursor.fetchall()

    def filtred_routes_in_to_city(self, city):
        db_connection = self.db.connect_to_db()
        cursor = db_connection.cursor()
        cursor.execute(
            f'SELECT src_airport, dst_airport, airplane FROM routes WHERE src_airport in (SELECT iata FROM airports WHERE city = \'{city}\')')
        return cursor.fetchall()


    # def routes_between_cities(self, citi1, city2):

if __name__ == '__main__':
    test = Controller_airports()
    res = test.filtred_airports(1, 5, 2, 10)
    res1 = test.filtred_routes_in_to_city('Moscow')
    print(res1)