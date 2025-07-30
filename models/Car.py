

class Car:
    cars = {
        "AUDI": [{"model": "A4", "production_year": 2004},
                 {"model": "A5", "production_year": 2004},
                 {"model": "A6", "production_year": 2004}
                 ],
        "BMW": [{"model": "M5", "production_year": 2006},
                {"model": "M3", "production_year": 2007}
                ],
        "MERCEDES": [{"model": "GLK", "production_year": 2008},
                     {"model": "GLE", "production_year": 2009}
                     ],
    }

    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__production_year = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("Brand needs to be set.")

        valid_models = [model["model"] for model in Car.cars[self.__brand]]

        if model.upper() not in valid_models:
            raise ValueError(f"{model.upper()} model is not available.")

        self.__model = model.upper()

        for car_model in Car.cars[self.__brand]:
            if car_model["model"] == model.upper():
                self.__production_year = car_model["production_year"]

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, year):
        if self.__model is None:
            raise ValueError("Production year can not be set.")

        if self.__model is not None and self.__production_year is not None:
            raise ValueError("Production year can not be set.")

        self.__production_year = year

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        valid_brands = [brand for brand, model in Car.cars.items()]
        if brand.upper() not in valid_brands:
            raise ValueError(f"{brand.upper()} brand is not available.")

        self.__brand = brand.upper()


audi = Car()
audi.brand = "Audi"
audi.model = "A6"

bmw_m5 = Car()
bmw_m5.brand = "bmw"
bmw_m5.model = "m5"
# bmw_m5.production_year = 2006

print(audi.brand, audi.model, audi.production_year)
print(bmw_m5.brand, bmw_m5.model, bmw_m5.production_year)
