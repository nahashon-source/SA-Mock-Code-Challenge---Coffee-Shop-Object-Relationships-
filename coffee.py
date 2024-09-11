from customer import Customer
from order import Order

class Coffee:
    def __init__(self):
        self.menu = {
            "tea": 2.5, "cappuccino": 2.0, "black coffee": 3.5,
            "latte": 3.0, "cold brew": 4.0, "barista": 1.25
        }
        self.inventory = {item: 10 for item in self.menu}  # Set initial inventory levels
        self.inventory["barista"] = 20  
        self.sales = 0.0  # Total sales
        self.customer = None  # Placeholder for the customer object
        self.order = Order()  # Initialize an order object

    def display_menu(self):
        """Displays the available menu items and their prices."""
        print("\n---- Menu ----")
        for item, price in self.menu.items():
            print(f"{item.capitalize()} : ${price:.2f}")
        print("------------------\n")

    def take_order(self):
        """Takes an order from the customer."""
        self.order.clear_order()  # Clear previous orders
        while True:
            self.display_menu()
            order_item = input(f"{self.customer.get_name()}, what would you like? (type 'done' to finish) ").lower()
            if order_item == 'done':
                break  # End ordering process if 'done' is entered
            if order_item in self.menu and self.inventory[order_item] > 0:
                try:
                    quantity = int(input("How many? "))  # Ask for the quantity of the item
                    if quantity <= self.inventory[order_item]:
                        self.order.add_item(order_item, quantity)  # Add to the order
                    else:
                        print(f"Only {self.inventory[order_item]} {order_item}(s) left.")
                except ValueError:
                    print("Invalid quantity.")  # Handle invalid quantity input
            else:
                print(f"{order_item} not available or out of stock.")
        self.process_order()  # Process the completed order

    def process_order(self):
        """Processes the order, calculates total cost, and updates inventory."""
        total_cost = sum(self.menu[item] * quantity for item, quantity in self.order.get_order().items())  # Calculate total cost
        print("\n--- Order Summary ---")
        for item, quantity in self.order.get_order().items():
            print(f"{quantity} x {item.capitalize()} = ${self.menu[item] * quantity:.2f}")  # Display order summary
        print(f"Total cost: ${total_cost:.2f}\n")
        
        if input("Proceed with the order? (yes/no) ").lower() == "yes":  # Confirm if the customer wants to proceed
            self.sales += total_cost  # Add total cost to sales
            for item, quantity in self.order.get_order().items():
                self.inventory[item] -= quantity  # Reduce the ordered items from inventory
            print(f"Thank you, {self.customer.get_name()}! Your order is placed.")
        else:
            print("Order cancelled.")  # Cancel the order if not confirmed

    def main(self):
        """Main program loop for interacting with the customer."""
        self.customer = Customer(input("Welcome! What's your name? ").capitalize())  # Get customer's name
        while True:
            # Display options to the customer
            print("\n1. Place order\n2. View Sales\n3. View Inventory\n4. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                self.take_order()  # Start ordering process
            elif choice == "2":
                print(f"\nTotal Sales: ${self.sales:.2f}")  # Display total sales
            elif choice == "3":
                # Display current inventory levels
                print("\n--- Inventory ---")
                for item, quantity in self.inventory.items():
                    print(f"{item.capitalize()}: {quantity}")
                print("-------------------")
            elif choice == "4":
                # Exit the program
                print(f"Thank you, {self.customer.get_name()}. Come Again")
                break
            else:
                print("Invalid option.")  