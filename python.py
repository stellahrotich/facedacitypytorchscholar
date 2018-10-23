#python revision
"""

Python is a programming language that lets you work quickly and
 integrate systems more effectively"""

print ("Hello,World!")

#Commenting in python
#we use to create single line comments in python and """ for multiple lines comments
#example
"""This is a
multiline docstring."""
#comments are used for code documantation
#Python uses triple quotes at the beginning and end of the docstring as shwoen above

print("Hello, World! Again")

#Variables
#Variables can be replaced once it has been created by assigning to another variable

x = 8 # x is of type int
x = "Sandra" # x is now of type str
print(x)

#Rules for variables in python

    #A variable name must start with a letter or the underscore character
    #A variable name cannot start with a number
    #A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    #Variable names are case-sensitive (age and  Age are different variables)

#python concatenation

#Python allows for command line input
#python revision
"""

Python is a programming language that lets you work quickly and
 integrate systems more effectively"""

print ("Hello,World!")

#Commenting in python
#we use to create single line comments in python and """ for multiple lines comments
#example
"""This is a
multiline docstring."""
#comments are used for code documantation
#Python uses triple quotes at the beginning and end of the docstring as shwoen above

print("Hello, World! Again")

#Variables
#Variables can be replaced once it has been created by assigning to another variable

x = 8 # x is of type int
x = "Sandra" # x is now of type str
print(x)

#Rules for variables in python

    #A variable name must start with a letter or the underscore character
    #A variable name cannot start with a number
    #A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    #Variable names are case-sensitive (age and  Age are different variables)

#python concatenation

#Python allows for command line input
#python revision
"""

Python is a programming language that lets you work quickly and
 integrate systems more effectively"""

print ("Hello,World!")

#Commenting in python
#we use to create single line comments in python and """ for multiple lines comments
#example
"""This is a
multiline docstring."""
#comments are used for code documantation
#Python uses triple quotes at the beginning and end of the docstring as shwoen above

print("Hello, World! Again")

#Variables
#Variables can be replaced once it has been created by assigning to another variable

x = 8 # x is of type int
x = "Sandra" # x is now of type str
print(x)

#Rules for variables in python

    #A variable name must start with a letter or the underscore character
    #A variable name cannot start with a number
    #A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    #Variable names are case-sensitive (age and  Age are different variables)

#python concatenation

#python revision
"""

Python is a programming language that lets you work quickly and
 integrate systems more effectively"""

print ("Hello,World!")

#Commenting in python
# This is a one-line Python comment - code blocks are so useful!
"""This type of comment is used to document the purpose of functions and classes."""

#Variables
#Variables can be replaced once it has been created by assigning to another variable

x = 8 # x is of type int
x = "Sandra" # x is now of type str
print(x)

#Rules for variables in python

    #A variable name must start with a letter or the underscore character
    #A variable name cannot start with a number
    #A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    #Variable names are case-sensitive (age and  Age are different variables)

#python concatenation

#Python XCollections(Arrays)

#Python allows for command line input
#A list is a collection which is ordered and changeable

fruits = ["apple", "banana", "cherry", "oranges", "mangoes", "avocados"]
print(fruits)

fruits.append("passion")

"""Lists Methods and 	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""

#Tuples
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#You cannot change values in a tuple:
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.
#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
#data types

boolean = True
number = 1.1
string = "Strings can be declared with single or double quotes."
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None

#Simple Logging

print "Printed!"

#Conditionals

if cake == "delicious":
    return "Yes please!"
elif cake == "okay":
    return "I'll have a small piece."
else:
    return "No, thank you."

#Loops

for item in list:
    print item

while (total < max_val):
    total += values[i]
    i += 2

#Functions

def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print q, r

#Classes

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1
      
      #functions
      |"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example1(manatees):
    for manatee in manatees:
        print manatee['name']

def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee
