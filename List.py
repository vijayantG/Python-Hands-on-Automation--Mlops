# Create an empty list using square brackets

from matplotlib.pylab import f


l1 = [] 
print("Empty List:", l1)


# Create a four-element list using square brackets

l2 = [10,20,"30", 40.5]

print("Four-element List:", l2)


# Create an empty list using the list() constructor

l3 = list()
print(l3)

# Create a three-element list from a tuple using the list() constructor

l4 =list((1,"two",3.0))

print (f"Three-element List from tuple: {l4}")


# Print out the first element of list l2

print(f"First element of l2: {l2[0]}")


# Assign the third and the fourth elements of l2 to a new list

l5 = l2[2:]

print(f"New list from third and fourth elements of l2: {l5}")


# Append a new element to the list l1
l1.append(l5)

print(f"l1 after appending l5 : {l1}")


# Remove element 30 from the list l1

l1[0].remove("30")
print(f"l1 after removing '30': {l1}")


# Change value at index 2 (third element) in l2

l2[2] = 30
print(f"l2 after changing third element: {l2}")