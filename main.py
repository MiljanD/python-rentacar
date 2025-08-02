from models.User import User
from models.Car import Car
from helper_functions.display import display_choices


# constants that are lists and each will be passed to display_choice function
OPTIONS = ["User Options", "Car Options", "Exit"]
USER_OPTIONS = ["Add user", "Show users"]
CAR_OPTIONS = ["Add new car", "Show all cars", "Rent car", "Show available cars", "Show rented cars"]


# variable that is responsible for running the program
is_running = True

# main loop
while is_running:
    # home screen choice of user or car section
    option_choice = display_choices(OPTIONS)

    # user section
    if option_choice == 1:
        user_option = display_choices(USER_OPTIONS)
        user = User()

        # adding new users
        if user_option == 1:
            user.name = input("Enter name: ")
            user.age = int(input("Enter age: "))
            user.create()

        # display of all users
        elif user_option == 2:
            print("Users list: ")
            user.show_users()

    # car section
    elif option_choice == 2:
        car_option = display_choices(CAR_OPTIONS)
        car = Car()
        # check is rent of some car expired
        car.return_from_rent()

        # adding of new car
        if car_option == 1:
            car.brand = input("Enter car brand: ")
            car.model = input("Enter car model: ")
            car.production_year = int(input("Enter year of production: "))
            car.add_car()

        # display list of all cars
        elif car_option == 2:
            car.show_all_cars()

        # renting of specific car
        elif car_option == 3:
            car_brand = input("Enter desired brand: ")
            car.rent_car(car_brand)

        # display list of all available cars
        elif car_option == 4:
            car.show_available_cars()

        # display list of all rented cars
        elif car_option == 5:
            car.show_rented_cars()

    # option to exit the program
    elif option_choice == 3:
        print("Exiting...")
        is_running = False


