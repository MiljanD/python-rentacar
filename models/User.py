from models.Db import Db


class User(Db):
    def __init__(self):
        super().__init__()

        con = super()._get_connection()
        self.__name = None
        self.__age = None


    def set_age(self, age):
        if age < 18:
            raise ValueError("User age must be 18 or more.")

        self.__age = age


    def get_age(self):
        return self.__age


    def get_name(self):
        return self.__name


    def set_name(self, name):
        if len(name) < 3:
            raise ValueError("Name must be at least 5 characters long")

        self.__name = name


toma = User()

toma.set_name("Tomislav")
print(toma.get_name())

toma.set_age(18)
print(toma.get_age())

