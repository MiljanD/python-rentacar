

# Helper function for consistent screen display
def display_choices(list_of_options):
    """
    Function is used to display consistent screen for all options
    :param list_of_options: list of options that needs to be displayed on the screen

    """
    print("Options:")
    for idx, option in enumerate(list_of_options):
        print(f"{idx + 1}. {option}")
    print()
    option_choice = int(input("Chose option: "))
    if option_choice > len(list_of_options) or option_choice <= 0:
        raise ValueError("Unavailable option.")

    return option_choice