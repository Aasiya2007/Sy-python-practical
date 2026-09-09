products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

name = input("Enter product name: ")

if name in products:
    print("Product found")
    print("Index:", products.index(name))
else:
    print("Product not found")