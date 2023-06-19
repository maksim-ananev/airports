import mysql.connector
from mysql.connector import Error

class DBConnector():
    def __init__(self):
        self.host = 'db4free.net'
        self.user = 'user_for_flights'
        self.passwd = 'simple_password'
        self.database = 'flights'
        self.connection = None

    def connect_to_db(self):
        if self.connection is None:
            try:
                connection = mysql.connector.connect(host=self.host,
                                                     user=self.user,
                                                     passwd=self.passwd,
                                                     database=self.database)

                if connection.is_connected():
                    self.connection = connection
                    return self.connection

            except Error as e:
                print('Error while connecting to MySQL', e)

        else:
            return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None




if __name__ == '__main__':
    test = DBConnector()
    test.connect_to_db()
    print('Ok')
