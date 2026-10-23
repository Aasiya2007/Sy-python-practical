items = {
    "apple": "Fruit",
    "carrot": "Vegetable",
    "rose": "Flower",
    "dog": "Animal"
}
key = input("Enter the key to search: ").strip()
try:
    value = items[key]
    print("Item found:", value)
except KeyError:
    print("Item Not Found")
