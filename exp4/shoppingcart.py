'''Shopping Cart Management System
1. Add Item to Cart
2. View Cart
3. Remove Item from Cart
4. Calculate Total Cost
5. Exit
Enter your choice (1-5): 1
Enter item code: ABC123
Enter quantity: 2
Item added to cart successfully!
Enter your choice (1-5): 2
Shopping Cart Contents:
Item Code: ABC123 | Item Name: Laptop | Price: $800.00 | Quantity: 2
Enter your choice (1-5): 4
Total Cost: $1600.00
Enter your choice (1-5): 3
Enter item code to remove: ABC123
Item removed from cart successfully!
Enter your choice (1-5): 5
Thank you for using the Shopping Cart Management System
This is the output of the program. Create a program for this using dictionaries not classes.'''

def add_item(cart, item_code, item_name, price, quantity):
    cart[item_code] = {'item_name': item_name, 'price': price, 'quantity': quantity}
    print('Item added to cart successfully!')

def view_cart(cart):
    print('Shopping Cart Contents:')
    for item_code, item in cart.items():
        print(f"Item Code: {item_code} | Item Name: {item['item_name']} | Price: ${item['price']:.2f} | Quantity: {item['quantity']}")

def remove_item(cart, item_code):
    if item_code in cart:
        del cart[item_code]
        print('Item removed from cart successfully!')
    else:
        print('Item not found in cart!')

def calculate_total_cost(cart):
    total_cost = sum(item['price'] * item['quantity'] for item in cart.values())
    print(f'Total Cost: ${total_cost:.2f}')

def main():
    cart = {}
    while True:
        print('1. Add Item to Cart')
        print('2. View Cart')
        print('3. Remove Item from Cart')
        print('4. Calculate Total Cost')
        print('5. Exit')
        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            item_code = input('Enter item code: ')
            item_name = input('Enter item name: ')
            price = float(input('Enter price: '))
            quantity = int(input('Enter quantity: '))
            add_item(cart, item_code, item_name, price, quantity)
        elif choice == '2':
            view_cart(cart)
        elif choice == '3':
            item_code = input('Enter item code to remove: ')
            remove_item(cart, item_code)
        elif choice == '4':
            calculate_total_cost(cart)
        elif choice == '5':
            print('Thank you for using the Shopping Cart Management System')
            break
        else:
            print('Invalid choice! Please enter a number between 1 and 5.')

if __name__ == '__main__':
    main()

# Output
# 1. Add Item to Cart
# 2. View Cart
# 3. Remove Item from Cart
# 4. Calculate Total Cost
# 5. Exit

