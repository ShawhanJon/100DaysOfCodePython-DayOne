###### The basic Print Function ######
print("Hello World!")
#Output:  Hello World!
print("\n")

###### New Line ######
print("Hello World!\nHello World!")
#Output:  Hello World!
#         Hello World!
print("\n")

###### Concatenation ######
print("Hello" + " " + "Jon")
#Output:  Hello Jon
print("\n")

###### String Manipulation & Debugging ######
print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + '"+"' + " sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
#Output:  Day 1 - String Manipulation
#         String Concatenation is done with the "+" sign.
#         e.g. print("Hello " + "world")
#         New lines can be created with a backslash and n.
print("\n")

###### Input Function ######
length = (input("What is your name? "))
print(len(length))
#Input:   Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr. (Longest Personal Name)
#Output:  53
print("\n")

###### Variables ######
name = "Jack"
print(name)

name = "Angela"
print(name)

name = input("What is your name? ")
length = len(name)
print(length)


a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)
#Input:  2
#        6
#Output:  a: 6
#         b: 2