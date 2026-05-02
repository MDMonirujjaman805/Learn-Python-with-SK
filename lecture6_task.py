# average of 3 numbers
def calc_avg(a, b, c):
    s = a + b + c
    a = s / 3
    return a


print(calc_avg(4, 4, 4))


# Practice Task 01: Write a Program to print the length of a list.(list is the parameter)
numbers = {3, 4, 5, 6, 7, 8, 9}
names = {"Monir", "Khaled", "Monirujjaman"}


def len_of_list(li):
    print(len(li))


len_of_list(numbers)
len_of_list(names)


# Practice Task 02: Write a Program to print the elements of a list in a single line.(list is the parameter)
def print_list_single_line(x):
    for item in x:
        print(item, end=" ")


print_list_single_line(names)
print()


# Practice Task 03: Write a Program to find the factorial of n.(n is the parameter)
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f)
    # return f


factorial(7)


# Practice Task 04: Write a Program to convert USD to BDT.
def converter(usd_val):
    bdt_bal = usd_val * 122
    print(usd_val, "USD =", bdt_bal, "BDT")


converter(100)


def converter2(num):
    if num % 2 == 0:
        print("The number is 'EVEN'")
    else:
        print("The number is 'ODD'")

    return # control return


converter2(50)
