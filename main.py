from models.User import User
from models.Car import Car
from helper_functions.display import display_choices


OPTIONS = ["User Options", "Car Options", "Exit"]
USER_OPTIONS = ["Add user", "Show users"]
CAR_OPTIONS = ["Add new car", "Show all cars", "Rent car", "Show available cars", "Show rented cars"]


is_running = True

while is_running:
    option_choice = display_choices(OPTIONS)

    if option_choice == 1:
        user_option = display_choices(USER_OPTIONS)
        user = User()

        if user_option == 1:
            user.name = input("Enter name: ")
            user.age = int(input("Enter age: "))
            user.create()

        elif user_option == 2:
            print("Users list: ")
            user.show_users()

    elif option_choice == 2:
        car_option = display_choices(CAR_OPTIONS)
        car = Car()
        car.return_from_rent()

        if car_option == 1:
            car.brand = input("Enter car brand: ")
            car.model = input("Enter car model: ")
            car.production_year = int(input("Enter year of production: "))
            car.add_car()

        elif car_option == 2:
            car.show_all_cars()

        elif car_option == 3:
            car_brand = input("Enter desired brand: ")
            car.rent_car(car_brand)

        elif car_option == 4:
            car.show_available_cars()

        elif car_option == 5:
            car.show_rented_cars()

    elif option_choice == 3:
        print("Exiting...")
        is_running = False


