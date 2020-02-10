# Tuple
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#
# Example
# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
#
# Example
# Return the item in position 1:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable.
#
# Example
# You cannot change values in a tuple:

# thistuple = ("apple", "banana", "cherry")
# thistuple[1] = "blackcurrant"
# # The values will remain the same:
# print(thistuple)

#a[0] = ("X",) + a[0][1:]
# As a is a list you can change values in it. Above code simply assigns a[0] a new tuple.
# a[0] = list(a[0])       #make a[0] mutable
# a[0][0] = "X"            #now new assignment will be valid
# a[0] = tuple(a[0])      #make a[0] again a tuple


# Erroare din cauza parantezelor rotunde ... nu ne lasa sa modificam nimic (tuples)...
# ...trebuie paranteze patrate

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
#
# Example
# Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    # You will learn more about for loops in out Python For Loops Chapter.


# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Example
# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


# Tuple Length
# To determine how many items a tuple has, use the len() method:

# Example
# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#
# Example
# You cannot add items to a tuple:

thistuple = ("apple", "banana", "cherry")
# thistuple[3] = "orange"  # This will raise an error
print(thistuple)


# Remove Items
# Note: You cannot remove items in a tuple.
#
#  Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
#
# Example
# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
#del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
#
# Example
# Using the tuple() method to make a tuple:

# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


# Tuple Methods
# Python has two built-in methods that you can use on tuples.
#
# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
