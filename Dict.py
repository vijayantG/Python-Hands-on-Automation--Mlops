
# Create dictionary with duplicate keys

d0 = {"1":1, "1":2}

print(d0)

# Create an empty dictionary using curly brackets

d1 = {}

print("Empty Dictionary:", d1)

# Create a two-element dictionary using curly brackets

d2 = { "One": {"1":1, "2":2}, "Two": {"3":3, "4": 4} } 

print("Two-element Dictionary:", d2)

# Create an empty dictionary using the dict() constructor

d3 = dict()

print(d3)

# Create a two-element dictionary using the dict() constructor

d3 = dict([("one", 1), ("two", 2)])

print("Two-element Dictionary using dict() constructor:", d3)


# Access the value associated with key "One" in dictionary d2

print(d2['One'])


# Add a new key-value pair to the dictionary d2

d2['Four'] = {"5":5, "6":6 }

print(f"d2 after adding new key-value pair: {d2}")


# Remove the key "Two" from the dictionary d2

d2.pop("Two")

print(f"d2 after removing key 'Two': {d2}")