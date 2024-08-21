'''Develop an e-commerce platform where sellers can list products, customers can browse
and purchase items, and administrators can manage orders, payments, and shipping
logistics.'''

def list_product(site, product_id, product_name, quantity, price):
    site[product_id] = {'product_name':product_name, 'quantity':quantity, 'price':price}

def browse(site):
    print("{:15}{:30}{:10}{:20}".format("Product ID", "Product Name", "Stock", "Price per Product"))
    for i in site.items():
        if i[1]['quantity']!=0:
            print("{:15}{:30}{:<10}{:<20.2f}".format(i[0],i[1]['product_name'],i[1]['quantity'],i[1]['price']))
        else:
            continue

def add_to_cart(cart, site, product_id, quantity):
    if site[product_id]['quantity'] >= quantity:
        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            cart[product_id] = {'product_name': site[product_id]['product_name'], 'quantity': quantity, 'price': site[product_id]['price']}
        print(f"Added {quantity} of {site[product_id]['product_name']} to cart")
    else:
        print("Out of Stock")

def remove_from_cart(cart, product_id, quantity):
    if product_id in cart:
        if cart[product_id]['quantity'] > quantity:
            cart[product_id]['quantity'] -= quantity
            print(f"Removed {quantity} of {cart[product_id]['product_name']} from cart")
        elif cart[product_id]['quantity'] == quantity:
            del cart[product_id]
            print(f"Removed {cart[product_id]['product_name']} from cart")
        else:
            print(f"Cannot remove {quantity} as only {cart[product_id]['quantity']} is in the cart")
    else:
        print("Product not in cart")

def checkout(cart, site, last_purchase):
    total = 0
    for product_id, details in cart.items():
        if site[product_id]['quantity'] >= details['quantity']:
            site[product_id]['quantity'] -= details['quantity']
            total += details['quantity'] * details['price']
            last_purchase[product_id] = details
        else:
            print(f"Not enough stock for {details['product_name']}")
    cart.clear()
    print(f"Total amount to be paid: ${total:.2f}")

def main():
    site = {}
    cart = {}
    last_purchase = {}
    while True:
        print("Ecommerce Website")
        print("\tWho are you?:\n\
                1.Seller\n\
                2.Customer\n\
                3.Administrator\n\
                4.Exit")
        role = int(input("Enter(1-4): "))
        if role == 1:
            product_id = input("enter product id: ")
            product_name = input("enter product name: ")
            product_quantity = int(input("enter stock of product: "))
            product_price = float(input("enter product price: "))
            list_product(site, product_id, product_name, product_quantity, product_price)
            print("Product successfully added/modified")

        elif role == 2:
            while True:
                print("\tCustomer Menu:\n\
                        1.Browse Products\n\
                        2.Add to Cart\n\
                        3.Remove from Cart\n\
                        4.Checkout\n\
                        5.Back to Main Menu")
                customer_choice = int(input("Enter(1-5): "))
                if customer_choice == 1:
                    browse(site)
                elif customer_choice == 2:
                    product_id = input("enter id of product to be purchased: ")
                    quantity = int(input("enter the quantity of the product to be purchased: "))
                    add_to_cart(cart, site, product_id, quantity)
                elif customer_choice == 3:
                    product_id = input("enter id of product to be removed: ")
                    quantity = int(input("enter the quantity of the product to be removed: "))
                    remove_from_cart(cart, product_id, quantity)
                elif customer_choice == 4:
                    checkout(cart, site, last_purchase)
                elif customer_choice == 5:
                    break
                else:
                    print("Invalid option")

        elif role == 3:
            print("Administrator")
            print("1. Manage Orders\n\
                    2. Manage Payments\n\
                    3. Manage Shipping Logistics")
            admin_role = int(input("Enter(1-3): "))
            if admin_role == 1:
                print("Manage Orders")
                print("{:15}{:30}{:10}{:20}".format("Product ID", "Product Name", "Stock", "Price per Product"))
                for i in site.items():
                    print("{:15}{:30}{:<10}{:<20.2f}".format(i[0], i[1]['product_name'], i[1]['quantity'], i[1]['price']))
            elif admin_role == 2:
                print("Manage Payments")
                print("1. View Payments\n\
                        2. Update Payments")
                payment_role = int(input("Enter(1-2): "))
                if payment_role == 1:
                    print("View Payments")
                    print("{:15}{:30}{:10}{:20}".format("Product ID", "Product Name", "Quantity", "Price"))
                    for product_id, details in last_purchase.items():
                        print("{:15}{:30}{:<10}{:<20.2f}".format(product_id, details['product_name'], details['quantity'], details['price'] * details['quantity']))
                elif payment_role == 2:
                    print("Update Payments")
                    print("No payments to update")
                else:
                    print("Invalid option")
            elif admin_role == 3:
                print("Manage Shipping Logistics")
                print("1. View Shipping\n\
                        2. Update Shipping")
                shipping_role = int(input("Enter(1-2): "))
                if shipping_role == 1:
                    print("View Shipping")
                    print("{:15}{:30}{:10}{:20}".format("Product ID", "Product Name", "Quantity", "Price"))
                    for product_id, details in last_purchase.items():
                        print("{:15}{:30}{:<10}{:<20.2f}".format(product_id, details['product_name'], details['quantity'], details['price'] * details['quantity']))
                elif shipping_role == 2:
                    print("Update Shipping")
                    print("No shipping to update")
                else:
                    print("Invalid option")
            else:
                print("Invalid option")

        elif role == 4:
            print("Thanks for Shopping")
            break

        else:
            print("invalid option")

if __name__ == '__main__':
    main()