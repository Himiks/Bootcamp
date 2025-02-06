import json
class Finances:
    def __init__(self):
        self.transactions = self.load_transactions()
        
        
    def load_transactions(self):
        try:
            with open("transactions.json") as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return []
        
        
    def add_transaction(self):
        type_transaction = input("Enter transaction type (income/expense): ")
        if not type_transaction or type_transaction not in ["income", "expense"]:
            raise ValueError("Transaction type must be 'income' or 'expense' ")
        amount = int(input("Input amount: "))
         
        if amount < 0:
            raise ValueError("Amount must be a positive number ")
        
        category = input("Enter a category (food, rent, salary): ")
        if not category:
            raise ValueError("Category is required ")
        
        date = input("Enter a date in format YYYY-MM-DD: ")
        
      
       
        transaction = {
            "type": type_transaction,
            "amount": amount,
            "category": category,
            "date": date
        }
        self.transactions.append(transaction)
        json_obj = json.dumps(self.transactions, indent=4)
        
        with open("transactions.json", "w") as file:
            file.write(json_obj)
            
    def view_transactions(self):
        for transaction in self.transactions:
            print("Transaction:")
            for key, value in transaction.items():
                print(f"  {key}: {value}")
                
            
    
    
    def financial_summary(self):
        
        total_income = 0
        total_expenses = 0
        for transaction in self.transactions:
            for key, value in transaction.items():
                if value == "expense":
                   total_expenses += transaction["amount"]
                elif value == "income":
                    total_income += transaction["amount"]
                
        print(f"Total expenses = {total_expenses}")
        print(f"Total Income = {total_income}")
            
        
        



transaction = Finances()

print("Enter your choice: ")
print("1. Add transaction")
print("2. View transaction")
print("3. Financial Summary")
print("4. Exit")


start = True

while start:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        transaction.add_transaction()
    elif choice == 2:
        transaction.view_transactions()
    elif choice == 3:
        transaction.financial_summary()
    elif choice == 4:
        start = False
    else:
        print("Wrong option, try again")
    
    
    









 
        
        
        