# Practice Task 01: Store following word meanings in a python dictionary:
# table: "a piece fo furniture","list of facts & figures"
# cat: "a small animal"
my_dict = {
    "table": ["a piece fo furniture", "list of facts & figures"],
    "cat": "a small animal",
}
print(my_dict)
print(type(my_dict))


# Practice Task 02: You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all students.
subjects = {
    "python",
    "java",
    "C++",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "C++",
    "C",
}
print(subjects)
class_rooms = print(len(subjects))

# Practice Task 03: Write a Program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.
marks = {}
x = int(input("Enter JS marks : "))
marks.update({"JS": x})
y = int(input("Enter TS marks : "))
marks.update({"TS": y})
z = int(input("Enter PY marks : "))
marks.update({"PY": z})
print(marks)

# Practice Task 03: Figure out a way to store 9 & 9.0 as separate values in the set.
data = {9, "9.0"}  # way - 1
print(data)

values = {("int", 9), ("float", 9.0)}  # way - 2
print(values)
