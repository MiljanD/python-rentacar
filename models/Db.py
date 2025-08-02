import pymysql

# Db class responsible to make connection to database
class Db:

    def __init__(self):
        self.__connection = pymysql.connect(
            host="localhost",
            user="root",
            password="dm3004^mk2606",
            database="rent_a_car",
            cursorclass=pymysql.cursors.DictCursor
        )

    def _get_connection(self):
        return self.__connection
