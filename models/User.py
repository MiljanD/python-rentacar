from models.Db import Db


class User(Db):

    ALL_USERS = []

    def __init__(self):
        super().__init__()
        self.con = self._get_connection()
        self.__name = None
        self.__age = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("User age must be 18 or more.")

        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        split_name = new_name.split()
        if len(split_name) < 2:
            raise ValueError("Name must be in format first last name")

        self.__name = new_name


    def create(self):
        if self.__name is None or self.__age is None:
            raise ValueError("Name or age are not set.")

        first_name = self.__name.split()[0].capitalize()
        last_name = self.__name.split()[1].capitalize()

        cursor = self.con.cursor()
        query = "INSERT INTO users (first_name, last_name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (first_name, last_name, self.__age))
        self.con.commit()
        cursor.close()

    def show_users(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM users")
        self.con.commit()

        results = cursor.fetchall()
        cursor.close()
        for idx, result in enumerate(list(results)):
            print(f"{idx + 1 }. {result["first_name"]} {result["last_name"]}, {result["age"]} years old.")


