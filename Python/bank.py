class Account:
    
    
    def __init__(self, act_num, balance):
        self.account = act_num
        self.balance = balance
        
        

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Not enough funds!")

    def get_balance(self):
        return self.balance
    


print("Hello: ")
num = int(input("Plase input your account number: "))
balance = int(input("Please print your balance: "))
acount = Account(num, balance)

deposit = int(input("How much money would you like to put on deposit "))
acount.deposit(deposit)

withdraw = int(input("How much money would you like to withdraw: "))
acount.withdraw(withdraw)
print(acount.get_balance())