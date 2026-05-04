class Student:  # class
    name = "Monir"
    age = 66
    marks = 88.99


s1 = Student()  # instance or instance of Object
print(s1.name)
print(type(s1))


# Static Methods
# Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,without permanently modifying it.
class Employee:
    @staticmethod  # decorator
    def hello():
        print("Hello Python........")


e1 = Employee()
e1.hello()


#! Important
# Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.
# Encapsulation: Wrapping data and functions into a single unit(object).
