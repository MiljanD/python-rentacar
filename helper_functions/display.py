

def display_choices(list_of_options):
    print("Options:")
    for idx, option in enumerate(list_of_options):
        print(f"{idx + 1}. {option}")
    print()
    option_choice = int(input("Chose option: "))
    if option_choice > len(list_of_options) or option_choice <= 0:
        raise ValueError("Unavailable option.")

    return option_choice