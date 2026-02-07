# Creating the Set by using curly braces

s1 = {1,2,3,4}

print("Set created using curly braces:", s1)


# Creating an  Set using the set() constructor

s2 = set([5,6,7,8])

print("Set created using set() constructor:", s2)



# Creating two new sets 

names1 = set(["Glory", "Tony", "Joel", "Dennis"])

names2 = set(["Morgan", "Joel", "Tony", "Emmanuel", "Diego"])

# Performing union operation on names1 and names2

s3 = names1.union(names2)

print(f"union of names1 and names2: {s3}")


# Perfomring the union operation using the '|' operator

s3= names1 | names2

print(f"union of names1 and names2 using '|' operator: {s3}")


# Intersection of two sets using the intersection() method

s4 = names1.intersection(names2)

print(f"intersection of names1 and names2: {s4}")


# Intersection of two sets using the '&' operator

s5 = names1 & names2

print(f"intersection of names1 and names2 using '&' operator: {s5}")


# Adding a new element to the set names1

s1.add("Abraham")

print(f"names1 after adding 'Abraham': {s1}")


# Removing an element from the set names2

names1.remove("Glory")

print(f"names1 after removing 'Glory': {names1}")