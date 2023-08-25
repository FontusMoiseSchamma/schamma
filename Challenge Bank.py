class BankAccount:
    
    def __init__(self, account_number, account_holder, initial_balance):
        if initial_balance < 500.00:
            print("Depo inisyal la pa dwe pi piti ke 500.0 HTG")
            return
        
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Ou pa ka retire (0)HTG sou kont ou.")
            return
        if amount > self.balance:
            print("Ou pa ka retire plis ke (",self.balance,")HTG sou kont ou.")
            return
        
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance:.2f} HTG"

# Kreye yon kont
account1 = BankAccount("00475869", "Fontus Moise Schamma", 15000.00)

# Depo
account1.deposit(600.00)

# Retire
account1.withdraw(300.00)

# Verifye balans
balance = account1.get_balance()

# Afiche enfòmasyon sou kont lan
print(account1)
