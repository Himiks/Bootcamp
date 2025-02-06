def customer_details(products):
    name = input("\nEnter your name: \n")

    email = input("\nEnter your email: \n")
 
    address = input("\nEnter your address: \n")  
   
    
    print("Please choose your order: \n")
    print("If you are done enter q \n")
    display_products(products)
    orderered = True
    order_list = []
    payment = 0
    discount = False
    
    
  
    order = input("Please enter product name: \n")
        
    while orderered:
        
        if any(product[0] == order for product in products):
            quantity = input("Please enter quantity: \n")
            for item in products:
                if item[0] == order:
                    order_list.append(order)
                    payment+=item[1] * int(quantity)         
        else:
            print(f"Sorry there is no such product {order}")
        order = input("Please enter product name: \n")
        
        if order == "q" or order == "Q":
            orderered = False
            if payment > 1400:
                payment-=200
                discount = True
                    
                    
    return name, email, address, order_list, payment, discount


def  display_products(Products):
    
    for item in Products:
        print(f"\nProduct: {item[0]} - {item[1]}$ \n")

    
    
    
    
def askPayment_Method():
    print("How would you like to pay: (Cash, PayPal, MasterCard) ")
    input("Select a method: ")
    print("Please confirm your pin: ")
    input("Pin: ")
    print("Thank you! Have a great day! ")



def proces_Payment(name, email, address, orders, payment, discount):
    print("Order Confirmation: ")
    print("-------------------------------")
    print(f"Name: {name} ")
    print()
    print(f"Email: {email} ")
    print()
    print(f"Address: {address} ")
    print()
    print("orders: ")
    
    for order in orders:
        print(order)
        
    print("------------------------------------------------")
    
    if discount:
        print(f"The amount of money to pay with discount: {payment} ")
    else:
        print(f"The amount of money to pay: {payment} ")
    askPayment_Method()
    
    
    

products = [["Iphone", 700], ["Ipad", 900], ["Computer", 1500]]
name, email, address, orders, payment, discount = customer_details(products)
proces_Payment(name, email, address, orders, payment, discount)
