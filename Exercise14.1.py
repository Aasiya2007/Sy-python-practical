
products = {
    "Electronics": 0,
    "Clothing": 0,
    "Food": 0,
    "Books": 0
}

print("----- PRODUCT SURVEY -----")

# Number of voters
n = int(input("Enter number of voters: "))

for i in range(n):
    print("\nAvailable categories:")
    
    categories = list(products.keys())

    for j in range(len(categories)):
        print(j + 1, ".", categories[j])

    choice = int(input("Enter your choice: "))

    if 1 <= choice <= len(categories):
        selected = categories[choice - 1]
        products[selected] += 1

        print("Vote recorded for", selected)
    else:
        print("Invalid choice!")

# Display results
print("\n----- SURVEY RESULTS -----")

for product in products:
    print(product, ":", products[product], "votes")

# Determine winner
winner = max(products, key=products.get)

print("\nWinner:", winner)
print("Votes:", products[winner])
