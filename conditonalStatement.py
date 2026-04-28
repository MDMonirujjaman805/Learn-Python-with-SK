marks = 50

if marks >= 80:
    print("Your Grade is A")
elif marks >= 65:
    print("Your Grade is B")
elif marks >= 50:
    print("Your Grade is C")
elif marks >= 40:
    print("Your Grade is D")
else:
    print("Your Grade is F")


# With logical operator
result = int(input("Enter Student marks "))

if result >= 80 and result <= 100:
    print("A")
elif result >= 70 and result < 80:
    print("B")
elif result >= 60 and result < 70:
    print("C")
elif result >= 50 and result < 60:
    print("D")
elif result >= 40 and result < 50:
    print("E")
else:
    print("F")
