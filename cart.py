class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"Added {quantity} {item}(s) to the cart.")

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] <= quantity:
                del self.items[item]
            else:
                self.items[item] -= quantity
            print(f"Removed {quantity} {item}(s) from the cart.")
        else:
            print(f"{item} not found in the cart.")

    def calculate_total(self):
        total_price = sum(quantity * self.get_item_price(item) for item, quantity in self.items.items())
        return total_price

    def get_item_price(self, item):
        # In a real-world application, you might look up the price of the item from a database or external source
        # For simplicity, let's assume we have hardcoded prices for some items
        prices = {
            "apple": 1.0,
            "banana": 0.5,
            "orange": 1.5,
            "mango": 2.0
        }
        return prices.get(item, 0)

# Create a ShoppingCart instance
cart = ShoppingCart()

# Menu for user interaction
while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item name: ").lower()
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        cart.add_item(item, price, quantity)
    elif choice == '2':
        item = input("Enter item name: ").lower()
        quantity = int(input("Enter quantity to remove: "))
        cart.remove_item(item, quantity)
    elif choice == '3':
        total_price = cart.calculate_total()
        print(f"Total price: ${total_price:.2f}")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")