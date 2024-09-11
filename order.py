class Order:
    def __init__(self):
        self.current_order = {}  # Dictionary to store items and their quantities

    def add_item(self, item, quantity):
        if item in self.current_order:
            self.current_order[item] += quantity  # Increment the quantity if item exists
        else:
            self.current_order[item] = quantity  

    def clear_order(self):
        self.current_order.clear()  # Clear all items from the order.

    def get_order(self):
        return self.current_order  # Return the current order as a dictionary.
