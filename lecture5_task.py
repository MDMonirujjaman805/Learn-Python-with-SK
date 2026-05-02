# Practice Task 01: Print numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1
print("Loop Ended. 01")

# Practice Task 02: Print numbers from 100 to 1.
j = 100
while j >= 1:
    print(j)
    j -= 1
print("Loop Ended. 02")

# Practice Task 03: Print the multiplication table of a number n.
k = 1
n = int(input("Enter an Integer number : "))
while k <= 10:
    print(n * k)
    k += 1
print("Loop Ended. 03")

# Practice Task 04: Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
number_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(number_list):
    print(number_list[idx])
    idx += 1
print("Loop Ended. 04")

# Practice Task 04: Search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)
numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = 25
while i < len(numbers):
    if numbers[i] == x:
        print("FOUND at idx", i)
    else:
        print("founding.....")
    i += 1
print("Loop Ended. 05")
