# Practice Task 01: Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
# class Student:
#     def __init__(self, name, marks):
#         self.name = name = name
#         self.marks = marks

#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your average marks is:", sum / 3)


# s1 = Student("Monir", marks=[99, 87, 66])
# s1.avg_marks()

# s2 = Student("Khaled", marks=[67, 87, 55])
# s2.avg_marks()

# s3 = Student("Monirujjaman", marks=[87, 55, 99])
# s3.avg_marks()


# Practice Task 02: create Account class with 2 attributes balance and account no. Create methods for debit,credit and printing the balance.
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def get_debit(self, amount):
        self.balance -= amount
        print("BDT", amount, "was debited.")
        print("Total balance = ", self.get_balance())

    def get_credit(self, amount):
        self.balance += amount
        print("BDT", amount, "was credited.")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(44000, 3344)
print("Your Balance is: ", acc1.balance)
print("Your account no: ", acc1.account_no)
acc1.get_debit(500)
acc1.get_credit(1000)
