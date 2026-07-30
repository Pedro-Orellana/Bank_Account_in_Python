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
        print("Get some money from your account today!")
        print()

        withdrawal_amount = input("How much money would you like to withdraw? (or type 'CANCEL' to go back): ")

        while(True):
            if(withdrawal_amount == "CANCEL"):
                print("Cancelling your transaction...")
                print()
                print("Going back to main menu...")
                return
            if(withdrawal_amount == ""):
                print("Please provide an answer")
                continue
            try:
                withdrawal_amount = float(withdrawal_amount)
                break
            except ValueError:
                print("Please provide a valid money amount")
                print()
                continue

        if(withdrawal_amount <= self.balance):
            #make withdrawal
            self.balance -= withdrawal_amount
        else:
            print("Looks like you're trying to withdraw more than you have:")
            print()
            print(f"current balance: ${self.balance:.2f}")
            print(f"withdrawal amount: ${withdrawal_amount:.2f}")
            print()

            while(True):
                answer = input(f"Would you like to withdraw ${self.balance:.2f} instead? y/n: ")
                if(answer == 'y' or answer == 'n'):
                    break
                else:
                    print("Please answer only with a 'y' for yes or a 'n' for no")

            if(answer == 'y'):
                #make a complete withdrawal
                self.balance = 0
                
            else:
                print()
                print("You chose to not make any withdrawals today")
                print("Going back to main menu...")
                print()
                return
            
        print("Transaction completed successfully!")
        print("Please take your money!")
        print("$$$")
        print()
        print(f"Current balance: ${self.balance:.2f}")
        print()
        print("Going back to main menu...")
            
            




    
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





    

