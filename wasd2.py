value = int(input("Enter a number!"))
if value % 2 == 0:
    print ("The number is even")
else: 
    print ("The number is odd")

if value % 4 == 0:
    print ("The number is divisible by 4")

lesser = int(input("Enter in a number!"))
checker = int(input("Enter a number that is lower than the former number"))

if lesser % checker == 0:
    print ("The numbers divide equally")
else:
    print ("The numbers do not divide equally")
