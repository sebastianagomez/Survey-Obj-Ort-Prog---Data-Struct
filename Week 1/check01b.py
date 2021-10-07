# 01 Prepare : Checkpoint B
# Stuent : Sebastian Gomez
# Instructor : Vaughn Poulson
# Write a Python 3 program that asks the user how old they are, displays that information back 
# and then informs them how old they will be on their next birthday.


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
nextAge = age + 1

print()

print(f'Hello {name}, you are {age} years old.')
print(f'On your next birthday, you will be {nextAge}.')