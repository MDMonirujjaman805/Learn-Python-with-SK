# Practice Task 01: Write a Program to ask the user to enter names of their 3 favorite movies and store them in a list.

# Way 01: Using Slicing.
favorite_movie1 = input("Enter your 1st favorite movie name. ")
favorite_movie2 = input("Enter your 2nd favorite movie name. ")
favorite_movie3 = input("Enter your 3rd favorite movie name. ")
store1 = favorite_movie1[0 : len(favorite_movie1)]
store2 = favorite_movie2[0 : len(favorite_movie2)]
store3 = favorite_movie3[0 : len(favorite_movie3)]
print([store1, store2, store3])

# Way 02: Using append Method.
store = []
favorite_movie4 = input("Enter your 1st favorite movie name. ")
favorite_movie5 = input("Enter your 2nd favorite movie name. ")
favorite_movie6 = input("Enter your 3rd favorite movie name. ")
store.append(favorite_movie4)
store.append(favorite_movie5)
store.append(favorite_movie6)
print(store)

# Short form Using append Method.
movies = []
movies.append(input("Enter your 1st favorite movie name. "))
movies.append(input("Enter your 2nd favorite movie name. "))
movies.append(input("Enter your 3rd favorite movie name. "))
print(movies)


# Practice Task 02: Write a Program to check if a list contains a palindrome of elements.
list1 = ["m", "a", "a", "m"]

copy_list = list1.copy()
copy_list.reverse()

if copy_list == list1:
    print("Palindrome")
else:
    print("NOT Palindrome")


# Practice Task 03: Write a Program to count the number of students with "A" grade in the following Tuple.
grade = ("C", "D", "A", "A", "B", "B", "D", "A", "B")
print(grade.count("A"))


# Practice Task 04: Write a Program to Store the above values in a list and sort them form "A" to "D" (ascending order).
sorted_grade = ["C", "D", "A", "A", "B", "B", "D", "A", "B"]
sorted_grade.sort()
print(sorted_grade)
