print("LOCATION COORDINATE PROCESSING SYSTEM")

locations = [
    ("Tasgon", 18.5204, 73.8567),
    ("Vita", 19.0760, 72.8777),
    ("Jath", 19.9975, 73.7898),
    ("Atapadi", 17.3850, 78.4867)
]

print("\n1. Original Locations:")
print(locations)

print("\n2. Indexing Tuple Elements:")
first_location = locations[0]

print("Complete Tuple:", first_location)
print("Name:", first_location[0])
print("Latitude:", first_location[1])
print("Longitude:", first_location[2])
print("Last Element:", first_location[-1])
print("Second Last Element:", first_location[-2])

print("\n3. Tuple Unpacking:")
name, latitude, longitude = first_location

print("Name:", name)
print("Latitude:", latitude)
print("Longitude:", longitude)

print("\n4. Tuple Slicing:")
print("Original Tuple:", first_location)
print("First Two Elements:", first_location[:2])
print("Last Two Elements:", first_location[1:])
print("Only Coordinates:", first_location[1:3])
print("Reverse Tuple:", first_location[::-1])

print("\n5. Sorted by Latitude:")
sorted_by_latitude = sorted(
    locations,
    key=lambda location: location[1]
)

for name, latitude, longitude in sorted_by_latitude:
    print(f"{name}: ({latitude}, {longitude})")

print("\n6. Sorted by Longitude:")
sorted_by_longitude = sorted(
    locations,
    key=lambda location: location[2]
)

for name, latitude, longitude in sorted_by_longitude:
    print(f"{name}: ({latitude}, {longitude})")

print("\n7. Tuple Mutability:")
print("Original Tuple:", first_location)
print("Tuples are immutable.")
print("Therefore, tuple elements cannot be changed directly.")