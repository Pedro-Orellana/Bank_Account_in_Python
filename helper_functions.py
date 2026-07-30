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
    

    print(f"Your name is {name} and your pin number is {number_pin} and the initial amount is ${initial_amount:.2f}")

    new_account = account.BankAccount(account.account_number, name, number_pin, initial_amount)
    account.registered_accounts.append(new_account)

    #incrementing the account number for next account
    account.account_number += 1
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


def print_all_accounts():
    print(*account.registered_accounts, sep="\n")
