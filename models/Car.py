from models.Db import Db
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Car class is responsible to ensure all necessary functionalities and options for car section of the program

class Car(Db):
    # initial dict of available cars not needed any more since all of them are in database
    cars = {
        "AUDI": [{"model": "A4", "production_year": 2004, "rented": False, "rented_until": None},
                 {"model": "A5", "production_year": 2004, "rented": False, "rented_until": None},
                 {"model": "A6", "production_year": 2004, "rented": False, "rented_until": None}
                 ],
        "BMW": [{"model": "M5", "production_year": 2006, "rented": False, "rented_until": None},
                {"model": "M3", "production_year": 2007, "rented": False, "rented_until": None}
                ],
        "MERCEDES": [{"model": "GLK", "production_year": 2008, "rented": False, "rented_until": None},
                     {"model": "GLE", "production_year": 2009, "rented": False, "rented_until": None}
                     ],
    }

    def __init__(self):
        super().__init__()
        self.con = self._get_connection()
        self.__brand = None
        self.__model = None
        self.__production_year = None

    # property of class Car which represent model of specific car brand
    @property
    def model(self):
        return self.__model

    # setter for model property of specific car brand
    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("Brand needs to be set.")

        self.__model = model.upper()

    # property of class Car which represent production year of specific car brand
    @property
    def production_year(self):
        return self.__production_year

    # setter for production year property of specific car brand
    @production_year.setter
    def production_year(self, year):
        if self.__model is None:
            raise ValueError("Production year can not be set.")

        if self.__model is not None and self.__production_year is not None:
            raise ValueError("Production year can not be set.")

        self.__production_year = year

    # property of class Car which represent specific car brand
    @property
    def brand(self):
        return self.__brand

    # setter for specific car brand property
    @brand.setter
    def brand(self, brand):
        self.__brand = brand.upper()


    # method for displaying all cars in our rent a car agency
    def show_all_cars(self):
        """
        by querying the database, we are getting list of all cars which is passed to
        show_cars method

        """
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM cars")
        results = cursor.fetchall()
        cursor.close()
        self.show_cars(results)


    def show_cars(self, car_list):
        """ Is used to print data from passed car_list
        :param car_list: is list of dictionaries extracted from database
        """
        car_brands = []
        for brand in car_list:
            if brand["brand"] not in car_brands:
                car_brands.append(brand["brand"])

        for idx, car_brand in enumerate(car_brands):
            print(f"{idx+1}. {car_brand}")
            for model in car_list:
                if model["brand"] == car_brand:
                    if not model["is_rented"]:
                        rented = "Model is available"
                    else:
                        current_date = datetime.now()
                        expiration_in = str(model["rented_until"] - current_date)
                        if "day" in expiration_in:
                            expiration_in = f"{expiration_in[:6].strip(",")}"
                        else:
                            print(expiration_in)
                            if expiration_in[1] != ":":
                                expiration_in = f"{expiration_in[:2]} hours and {expiration_in[3:5]} minutes"
                            else:
                                expiration_in = f"{expiration_in[0]} hours and {expiration_in[2:4]} minutes"
                        rented = f"Model is still rented for {expiration_in}"

                    print(f"    * Model: {model["model"]} - Year of production: {model["production_year"]} - {rented}.")


    def add_car(self):
        """
        Method that enable us to add new car to out fleet
        """
        cursor = self.con.cursor()
        query = ("INSERT INTO cars (brand, model, production_year, is_rented, rented_until)"
                 "VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(query, (self.__brand, self.__model, self.__production_year, False, None))
        self.con.commit()
        cursor.close()


    def rent_car(self, brand_name):
        """
        Method that enable option of renting the specific car(brand/model)
        :param brand_name: parameter that is passed by user and represents specific car brand
        """
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM cars WHERE brand = %s AND is_rented = %s", (brand_name, False))
        self.con.commit()
        results = cursor.fetchall()

        if not results:
            print("Chosen brand name is not available.")
        else:
            self.show_cars(results)

            model_id = None
            rented = True
            model_choice = input("Chose model from the list: ")

            for model in results:
                if model["model"] == model_choice:
                    if not model["is_rented"]:
                        model_id = model["id"]
                        rented = False

            if not model_id:
                print("You have chose incorrect model.")
            else:
                if rented:
                    print("Model is already rented.")
                else:
                    days_of_rent = int(input("Number of renting days: "))
                    current_date = datetime.now()
                    rent_expiration = current_date + relativedelta(days=days_of_rent)

                    cursor.execute("UPDATE cars SET is_rented = %s, rented_until = %s WHERE id=%s", (True, rent_expiration, model_id))
                    self.con.commit()
                    cursor.close()


    def return_from_rent(self):
        """
        Method that checks whether renting of specific car is finished and restarts
        database records of is_rented and rented_until to default values

        """
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM cars WHERE is_rented = TRUE")
        self.con.commit()

        results = cursor.fetchall()

        current_date = datetime.now()

        for result in results:
            if result["rented_until"] <= current_date:
                cursor.execute("UPDATE cars SET is_rented = %s, rented_until = %s WHERE id = %s", (False, None, result["id"]))
                self.con.commit()

        cursor.close()


    def show_rented_cars(self):
        """
        Method that displays rented car list by using show_car method

        """
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM cars WHERE is_rented = %s", True)
        self.con.commit()

        results = cursor.fetchall()
        cursor.close()

        self.show_cars(results)


    def show_available_cars(self):
        """
        Method that displays available car list by using show_car method

        """
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM cars WHERE is_rented = %s", False)
        self.con.commit()

        results = cursor.fetchall()
        cursor.close()

        self.show_cars(results)



# This method is commented since it was used only to populate database from initial available cars dictionary

#     def add_cars_from_list(self):
#         cursor = self.con.cursor()
#         for brand, models in Car.cars.items():
#             for model in models:
#
#                 query = ("INSERT INTO cars (brand, model, production_year, is_rented, rented_until)"
#                          "VALUES (%s, %s, %s, %s, %s)")
#                 cursor.execute(query, (brand, model["model"], model["production_year"], model["rented"], model["rented_until"]))
#                 self.con.commit()
#         cursor.close()

