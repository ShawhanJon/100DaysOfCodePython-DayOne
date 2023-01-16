#1. Create a greeting for the program. Change to Business Name Generator.

print("Hello World(or you)!\n\nWelcome to the Business Name Generator.\nTwo simple questions to get your Business name!\n")

#2. Ask the user for the city they grew up in. Changed to favorite city.

print("----- Question #1 -----\n")
cityInput = input("What is your favorite city?\n")

#3. Ask the user for their pets name. Changed to industry

print("\n----- Question #2 -----\n")
industryInput = input("What industry are you in?\n")

#4. Combine the name of their city and pet and show them their band name.
#    Changed to combining the city and industry.

outTake = "\n\nYour business name could be "

print(outTake + "\n\t\t\t" + cityInput + " " + industryInput)

#5. Make sure the input cursor shows on a new line.








# ###### The basic Print Function ######
# print("Hello World!")
# #Output:  Hello World!
# print("\n")

# ###### New Line ######
# print("Hello World!\nHello World!")
# #Output:  Hello World!
# #         Hello World!
# print("\n")

# ###### Concatenation ######
# print("Hello" + " " + "Jon")
# #Output:  Hello Jon
# print("\n")

# ###### String Manipulation & Debugging ######
# print("Day 1 - String Manipulation")
# print("String Concatenation is done with the " + '"+"' + " sign.")
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")
# #Output:  Day 1 - String Manipulation
# #         String Concatenation is done with the "+" sign.
# #         e.g. print("Hello " + "world")
# #         New lines can be created with a backslash and n.
# print("\n")

# ###### Input Function ######
# length = (input("What is your name? "))
# print(len(length))
# #Input:   Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr. (Longest Personal Name)
# #Output:  53
# print("\n")

# ###### Variables ######
# name = "Jack"
# print(name)

# name = "Angela"
# print(name)

# name = input("What is your name? ")
# length = len(name)
# print(length)


# a = input("a: ")
# b = input("b: ")
# c = a
# a = b
# b = c
# print("a: " + a)
# print("b: " + b)
# #Input:  2
# #        6
# #Output:  a: 6
# #         b: 2