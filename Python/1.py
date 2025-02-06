def customer_details():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")  
    
    print("Please choose your order: ")
    display_products(Products)
    
    
    
    return name, email, address


def display_products(Products):
    print("Available products: ")
    for category, items in Products.items():
        print(f"{category}: ")
        if isinstance(items, list):
            for item in items:
                print(f"Model {item[0]}: ${item[1]}")
        elif isinstance(items, dict):
            for model, price in items.items():
                print(f" {model}: ${price}")
        else:
            print(f" {items}")
    
            
                
        
    



Products = {
    "Iphone": [[11, 450], [12, 650], [13, 750], [14, 800], [15, 900]],
    "Ipad": {"Pro": 700, "Mini" : 500, "Max" : 1000},
    "Headphones": [[1, 70], [2, 150], [3, 250]]
}

name, email, address = customer_details(Products)  







    