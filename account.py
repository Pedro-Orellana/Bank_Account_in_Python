class BankAccount:

    def __init__(self, pin, name, password, amount):
        self.pin = pin
        self.name = name
        self.password = password
        self.amount = amount


    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount):
        self.amount -= amount

    

