#variables
registered_accounts = []
logged_account = None
account_number = 5000


class BankAccount:

    #dunder
    def __init__(self, account_number, name, pin, balance):
        self.pin = pin
        self.name = name
        self.balance = balance
        self.account_number = account_number
    
    def __repr__(self):
        return f"Account number: {self.account_number}, Name: {self.name}, pin number: {self.pin}, current balance: ${self.balance:.2f}"


    def make_deposit(self):

        if(logged_account == None):
            return
        
        print("Make a deposit to your account today!")
        while(True):
            deposit_amount = input ("Please enter the amount you want to deposit (or type 'CANCEL' to go back): ")
            if(deposit_amount == "CANCEL"):
                return
            try:
                deposit_amount = float(deposit_amount)
                break
            except ValueError:
                print("Please enter a valid number")
                print()

        #make the actual deposit
        logged_account.balance += deposit_amount
        print("You have successfully made a deposit to your bank account!")
        print(f"Your current balance is ${logged_account.balance:.2f}")
        print()

    def make_withdrawal(self):
        print("Trying to make a withdrawal...")
        print()
    
    def get_account_details(self):
        print("These are your account details:")
        print()
        print(f"Account owner: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Account pin: {self.pin}")
        print(f"Current balance: ${self.balance:.2f}")
        print()

    def logout(self):
        print("Logging out of your account...")
        print()
        logged_account = None





    

