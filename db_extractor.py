from db_connector import DBConnector

class db_extractor():
    def __init__(self):
        self.db = DBConnector()


    def get_cities(self):
        db_connection = self.db.connect_to_db()
        cursor = db_connection.cursor()
        cursor.execute(f'SELECT DISTINCT city FROM airports ORDER BY city ASC')
        result = [city for cities in cursor.fetchall() for city in cities]
        return result

if __name__ == '__main__':
    test = db_extractor()
    print('result ', test.get_cities())