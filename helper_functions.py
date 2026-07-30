
#main menu functions

def create_new_account():
    print()
    print("Creating new account!")
    print("Returning to main menu...")
    print()
    return

def account_login():
    print()
    print("Loging in to account!")
    print("Returning to main menu...")
    print()

def exit_program():
    print("\n")
    print("Exiting program!")



# helper functions

def get_valid_menu_option(input: str, start: int, stop: int):
    if(not input.isdigit()):
       print("Please enter a valid number")
       return -1

    number = int(input)
    if(number < start or number > stop):
        print("That number is not part of the options")
        return -1

    return number
