# Define a dictionary to store product information
products = {}

# Function to add a new product
def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    products[product_id] = {
        'name': name,
        'price': price,
        'stock': stock,
        'sales': 0
    }
    print(f"Product {name} added successfully.")

# Function to update stock levels during an order
def order_product():
    product_id = input("Enter product ID to order: ")
    quantity = int(input("Enter quantity to order: "))
    if product_id in products:
        if products[product_id]['stock'] >= quantity:
            products[product_id]['stock'] -= quantity
            products[product_id]['sales'] += quantity
            print(f"Ordered {quantity} of {products[product_id]['name']}")
        else:
            print("Not enough stock available")
    else:
        print("Product not found")

# Function to update stock levels during a return
def return_product():
    product_id = input("Enter product ID to return: ")
    quantity = int(input("Enter quantity to return: "))
    if product_id in products:
        products[product_id]['stock'] += quantity
        products[product_id]['sales'] -= quantity
        print(f"Returned {quantity} of {products[product_id]['name']}")
    else:
        print("Product not found")

# Function to generate reports on sales and inventory turnover
def generate_report():
    for product_id, info in products.items():
        turnover = info['sales'] * info['price']
        print(f"Product: {info['name']}, Sales: {info['sales']}, Turnover: ${turnover:.2f}, Stock: {info['stock']}")

# Main menu-driven program
def main():
    while True:
        print("\nMenu:")
        print("1. Add Product")
        print("2. Order Product")
        print("3. Return Product")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            order_product()
        elif choice == '3':
            return_product()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()