####################################################################################
#     JAMES LU MILLARD P2                                                          #
#    1. Create a program that asks the user to enter their name and their age.     #
#    Print out a message addressed to them that tells them the year that they      #
#    will turn 100 years old.                                                      #
#    2. Add on to this program by asking the user for another number and           #
#    printing out that many copies of the message.                                 #
#    3. Print out each copy of the message on separate lines. (Hint: the           #
#     string \n is the same as pressing the ENTER button)                          #
#################################################################################### 

name = input("what is your name?")
age = int(input("What is your age?"))
year = 2021
goal = 100
yeartooold = str((year-age)+goal)

print("You will be 100 years old in year:     " + yeartooold)

reprint= int(input("How many times do you want to reprint?"))
number = ("How many times do you want to reprint?\n")
number = number * int(reprint)
print(number)