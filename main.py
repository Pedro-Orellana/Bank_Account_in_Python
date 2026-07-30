import account
import helper_functions


#variables
main_menu_option = -1

print("Welcome to the Python Bank Program!")
print("\n")

while(main_menu_option != 3):
    print("Please select an option from the following list: ")
    print("1. Create a new account")
    print("2. Log in to your account")
    print("3. Exit the program")

    
    while (main_menu_option < 0):
        option_input = input("Type your selection here: ")
        main_menu_option = helper_functions.get_valid_menu_option(option_input, 1, 3)

    match main_menu_option:
        case 1:
            helper_functions.create_new_account()
        case 2:
            helper_functions.account_login()
        case 3:
            helper_functions.exit_program()

print("Exiting program")
print("Goodbye!")



