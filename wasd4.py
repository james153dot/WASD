divisor = 1
giveme = int(input('Please enter a number: '))
while divisor < giveme:
    divisor += 1
    if giveme % divisor == 0:
        print(divisor)