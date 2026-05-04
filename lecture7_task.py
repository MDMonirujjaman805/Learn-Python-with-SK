# Practice Task 01: Create a new file "practice1.txt" using python.Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

with open("practice1.txt", "w") as f:
    f.write(
        "Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java."
    )


# Write a Function that replace all occurrences of "Java" with "Python" in above file.
def check_for_word():
    with open("practice1.txt", "r") as g:
        data = g.read()

    new_data = data.replace("Java", "Python")
    print(new_data)

    with open("practice1.txt", "w") as h:
        h.write(new_data)

    # Search if the word "learning" exists in the file or not.
    word = "learning"
    with open("practice1.txt", "r") as i:
        d = i.read()
        if d.find(word) != -1:
            print("FOUND")
        else:
            print("NOT FOUND")


check_for_word()


# Practice Task 02: Write a Function to find in which line of the file does the word "learning" occur first. (Print -1 if word not found.)
with open("practice2.txt", "w") as o:
    o.write("2,3,4,5,6,7,8")


def find_learning():
    word2 = "learning"
    with open("practice2.txt", "r") as j:
        k = j.readline()
        if (k.find(word2)) != -1:
            print(1)
        else:
            print(-1)


find_learning()

# From a file containing numbers separated by comma,print the count of even numbers.
count = 0
with open("practice2.txt", "r") as n:
    m = n.read()
    print(m)

    # with split method
    nums = m.split(",")
    for val in nums:
        if int(val) % 2 == 0:
            count += 1
print(count)

# # without split method
# # num = ""
# # for i in range(len(m)):
# #     if m[i] == ",":
# #         print(int(num))
# #         num = ""
# #     else:
# #         num += m[i]
