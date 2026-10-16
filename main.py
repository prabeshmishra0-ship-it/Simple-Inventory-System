
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product Name:", self.name)
        print("Price: $", format(self.price, ".2f"))
        print("Available Quantity:", self.quantity)

    def update_quantity(self, amount):
        if self.quantity + amount >= 0:
            self.quantity += amount
            print("Quantity updated successfully.")
        else:
            print("Error: Not enough stock available.")

    def total_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added to inventory.")

    def display_inventory(self):
        if not self.products:
            print("The inventory is empty.")
            return

        print("\n--- Inventory Details ---")
        for product in self.products:
            product.display_info()
            print("--------------------")

    def calculate_total_value(self):
        total = 0
        for product in self.products:
            total += product.total_value()
        return total


def main():
    inventory = Inventory()

    product1 = Product("Laptop", 800.00, 5)
    product2 = Product("Mouse", 25.00, 10)
    product3 = Product("Keyboard", 45.00, 8)

    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    inventory.display_inventory()

    print("\n--- Updating Quantity ---")
    product1.update_quantity(-1)  # One laptop sold
    product2.update_quantity(5)   # Five mice restocked

    inventory.display_inventory()

    print("\nTotal Inventory Value: $",
          format(inventory.calculate_total_value(), ".2f"))

    print("\n--- Add a New Product ---")
    name = input("Enter product name: ")

    try:
        price = float(input("Enter product price: $"))
        quantity = int(input("Enter product quantity: "))

        if price < 0 or quantity < 0 or not name.strip():
            print("Please enter a valid name, price, and quantity.")
        else:
            new_product = Product(name, price, quantity)
            inventory.add_product(new_product)

            print("\n--- Updated Inventory ---")
            inventory.display_inventory()

            print("\nUpdated Total Inventory Value: $",
                  format(inventory.calculate_total_value(), ".2f"))

    except ValueError:
        print("Invalid input. Please enter a valid price and whole number quantity.")

    return


if __name__ == "__main__":
    main()
