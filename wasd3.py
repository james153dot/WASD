a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

lessthan_list = []

for item in a:

    if item < 5:

        lessthan_list.append(item)
print(lessthan_list)

lessthan = int(input("What numbers in the list are less than this value you are inputting?"))

lesserthan_list = []

for item in a:
    if item < lessthan:

        lesserthan_list.append(item)
print(lesserthan_list)