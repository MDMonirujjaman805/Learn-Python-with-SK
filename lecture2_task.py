# Practice Task 01: Write a Program to input user's first name and print its length.
first_name = input("Please, Enter your First name.")
length_first_name = len(first_name)
print("length of your name is ", length_first_name)

# Practice Task 02: Write a Program to find the occurrence of '$' in a String.
sentence = "Hi $ this is $ symbol, this price is $ 99 usd."
result = sentence.count("$")
print("The count of $ symbol is ", result)

# Practice Task 03: Write a Program to check if a number entered by the user is odd or even.
number = int(input("Enter a Integer Number "))
if number % 2 == 0:
    print("The number is EVEN.")
else:
    print("The number is ODD.")

# Practice Task 04: Write a Program to find the greatest of 3 numbers entered by the user.
a = int(input("Enter First Integer Number "))
b = int(input("Enter Second Integer Number "))
c = int(input("Enter Third Integer Number "))
if a > b and a > c:
    print("The First number Greater then Second and Third numbers. ", a)
elif b > a and b > c:
    print("The Second number Greater then First and Third numbers. ", b)
else:
    print("The Third number Greater then First and Second numbers. ", c)

# Practice Task 05: Write a Program to find the greatest of 4 numbers entered by the user.
w = int(input("Enter First Integer Number "))
x = int(input("Enter Second Integer Number "))
y = int(input("Enter Third Integer Number "))
z = int(input("Enter Fourth Integer Number "))
if w > x and w > y and w > z:
    print("The First number Greater then Second,Third and Fourth numbers. ", w)
elif x > w and x > y and x > z:
    print("The Second number Greater then First,Third and Fourth numbers. ", x)
elif y > w and y > x and y > z:
    print("The Third number Greater then First,Second and Fourth numbers. ", y)
else:
    print("The Fourth number Greater then First,Second and Third numbers. ", z)

# Practice Task 06: Write a Program to check if a number is a multiple of 7 or not.
m = int(input("Enter a number: "))
if m % 2 == 0:
    print("Multiple of 7")
else:
    print("Not Multiple of 7")
