from coffee import Coffee
from customer import Customer
from order import Order

def setup_coffees():
    # Initialize a list of coffee options with their prices
    coffee_list = [
        ("Americano", 2.5),
        ("Flat White", 3.5),
        ("Iced Late", 4.0),
        ("Mocha", 8.9),
        ("Black Coffee", 9.0)
    ]
    # Create Coffee instances from the coffee_list
    for name, price in coffee_list:
        Coffee(name, price)

def view_menu():
    # Display the list of available coffees
    print("\nAvailable Coffees:")
    print(Coffee.display_menu())

def get_customer():
    # Prompt user to enter their name and create a Customer instance
    name = input("Please enter your name: ")
    return Customer(name)

def get_coffee_choice():
    # Prompt user to choose a coffee and return the corresponding Coffee instance
    coffee_name = input("\nWhich coffee would you like to order? ")
    coffee = next((c for c in Coffee.all_coffees if c.name.lower() == coffee_name.lower()), None)
    if coffee is None:
        print("Sorry, we don't have that coffee. Please choose from the menu.")
    return coffee

def place_order():
    # Handle the process of placing an order
    customer = get_customer()  # Get customer details
    view_menu()  # Display coffee menu
    
    while True:
        coffee = get_coffee_choice()  # Get coffee choice
        if coffee:
            # Create an Order instance and display confirmation
            order = Order(customer, coffee, coffee.price)
            print(f"\nOrder placed successfully!")
            print(order)
            # Ask if the user wants to place another order
            if input("\nWould you like to place another order? (yes/no): ").strip().lower() != 'yes':
                break

def view_sales():
    # Display all orders and total sales
    if not Order.all_orders:
        print("\nNo orders have been placed yet.")
        return
    
    total_sales = sum(order.price for order in Order.all_orders)  # Calculate total sales
    print("\nAll Orders:")
    for order in Order.all_orders:
        print(order)
    
    print(f"\nTotal Sales: ${total_sales:.2f}")

def view_inventory():
    # Display all available coffee options
    if not Coffee.all_coffees:
        print("\nNo coffee available.")
        return
    
    print("\nCoffee Inventory:")
    for coffee in Coffee.all_coffees:
        print(coffee)

def display_menu():
    # Display the main menu options
    print("\n--- Coffee Shop Menu ---")
    print("1. Place Order")
    print("2. View Sales")
    print("3. View Inventory")
    print("4. Exit")

def main():
    setup_coffees()  # Initialize coffee options
    
    while True:
        display_menu()  # Show the main menu
        choice = input("Please select an option (1-4): ")
        
        if choice == "1":
            place_order()  # Handle placing an order
        elif choice == "2":
            view_sales()  # Show sales information
        elif choice == "3":
            view_inventory()  # Show inventory of coffees
        elif choice == "4":
            print("Enjoy your coffee!")  # Exit message
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()  