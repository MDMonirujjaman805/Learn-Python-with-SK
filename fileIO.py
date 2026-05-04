f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

g = open("demo.txt", "w")
g.write("I want to learn JavaScript tomorrow.")
g.close()

h = open("demo.txt", "a")
h.write(" 123")
h.close()


with open("lecture8_task.py", "w") as f:
    data = f.write(
        "# Practice Task 01: Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average."
    )

print(data)
