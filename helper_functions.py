import account

#main menu functions
def create_new_account():
    print()
    print("Thank you for opening an account with us!")
    print("Let's the necessary information")
    print()

    while(True):
        name = str(input("Please provide your full name (or type 'CANCEL' to go back to main menu): "))
        if(name == "CANCEL"):
            return
        if (name == ""):
            print("Please type your name before continuing")
            continue
        else:
            break

    print(f"Thank you, {name}")

    while(True):
        pin = input("please create your pin number: ")
        if(not pin.isdigit()):
            print("Please provide a valid number")
            continue
        number_pin = int(pin)
        if(number_pin < 1000 or number_pin > 9999):
            print("Pin number must be exactly 4 digits long")
            continue
        else:
            break

    while(True):
        initial_amount = input("Please your initial deposit (or '0' if you want to open an empty account) ")
        if(not initial_amount.isdigit()):
            print("Please type a valid number")
            continue
        else:
            initial_amount = float(initial_amount)
            break
    

    new_account = account.BankAccount(account.account_number, name, number_pin, initial_amount)
    account.registered_accounts.append(new_account)

    #incrementing the account number for next account
    account.account_number += 1

    print()
    print(f"Thank you, {name}, your account was succesfully created!")
    print()
    return

def account_login():
    print()
    print("Loging in to your account!")

    while(True):
        name = input("Please provide the name in your account (or type 'CANCEL' to go back to main menu): ")
        if(name == "CANCEL"):
            return
        if(name == ""):
            print("Please provide a valid name")
            continue
        else:
            break
    
    print(f"Welcome, {name}")

    while(True):
        pin = input("Please provide your pin number: ")
        if(not pin.isdigit()):
            print("Please provide a valid number")
            continue
        pin = int(pin)
        if(pin < 1000 or pin > 9999):
            print("Your pin number must be a 4-digit number")
            continue
        else:
            break

    #check if the account exists in the list of accounts
    for current_account in account.registered_accounts:
        if(current_account.name == name and current_account.pin == pin):
            account.logged_account = current_account

    if(account.logged_account == None):
        print()
        print("No account exists with that name and pin combination")
        print("Returning to main menu...")
        return

    print()
    print("Successfully logged in to your account!")
    print()

    user_menu_option = 0

    while(user_menu_option != 4):
        print("Please choose from the following menu:")
        print("1. Make a deposit to your account")
        print("2. Make a withdrawal from your account")
        print("3. Get account details")
        print("4. Log out from your account")

        while(True):
            str_option = input("Please type your selection: ")
            user_menu_option = get_valid_menu_option(str_option, 1, 4)
            if(user_menu_option > 0):
                break


        match (user_menu_option):
                case 1:
                    account.logged_account.make_deposit()
                case 2:
                    account.logged_account.make_withdrawal()
                case 3:
                    account.logged_account.get_account_details()
                case 4:
                    account.logged_account.logout()
                

    print("Going back to main menu...")

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


def print_all_accounts():
    print(*account.registered_accounts, sep="\n")
