# Inventory Tracking System

inventory = {}

def add_stock():
    product = input("Enter product name: ").strip()

    quantity = int(input("Enter quantity to add: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity

    print(quantity, product, "added successfully!")
    print("Current stock:", inventory[product])


def register_sale():
    product = input("Enter product name: ").strip()

    if product not in inventory:
        print("Product not found in inventory.")
        return

    quantity = int(input("Enter quantity sold: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
    elif quantity > inventory[product]:
        print("Not enough stock available.")
    else:
        inventory[product] -= quantity
        print("Sale registered successfully!")
        print("Remaining", product, "stock:", inventory[product])


def display_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\n===== CURRENT INVENTORY =====")

        for product, quantity in inventory.items():
            print(product, ":", quantity)


def main():
    while True:
        print("\n===== SHOP INVENTORY SYSTEM =====")
        print("1. Add Stock")
        print("2. Register Sale")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock()

        elif choice == "2":
            register_sale()

        elif choice == "3":
            display_inventory()

        elif choice == "4":
            print("Thank you for using the Inventory System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
