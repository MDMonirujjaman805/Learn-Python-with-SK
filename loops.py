# While Loop
count = 1  # iterator
while count <= 5:  # stopping condition
    print("Hello Python.....")
    count += 1  # update value
print("loop ended.")

i = 5
while i >= 1:
    print(i)
    i -= 1
print("loop ended.")

a = 1
while a <= 20:
    print(a)
    if a == 5:
        break
    a += 1

numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = 25
while i < len(numbers):
    if numbers[i] == x:
        print("FOUND at idx", i)
        break
    else:
        print("founding.....")
    i += 1
print("End of Loop.")


# For Loop
numbers2 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for num in numbers2:
    print(num)

text = ["monir", "Bangladesh", "js", "python"]
for t in text:
    print(t)
