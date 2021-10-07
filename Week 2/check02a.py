# 02 Prepare : Checkpoint A

# Stuent : Sebastian Gomez

# Instructor : Vaughn Poulson

# Write a Python 3 program that prompts the user for 3 postive numbers (or zero) and then adds them together. If the user enters a negative number, 
# the program should reprompt them until they enter a postive number.

def get_positive_number():
    num = -1
    while num < 0:
        num = int(input("\nEnter a positive number: "))
        if num >= 0:
            return num
        else:
            prompt_number()       

def prompt_number():
    print("\nInvalid entry. The number must be positive.")

def compute_sum(num1, num2, num3):
    return num1 + num2 + num3

def main():
    num1 = get_positive_number()
    num2 = get_positive_number()
    num3 = get_positive_number()

    result = compute_sum(num1, num2, num3)
    print (f"\nThe sum is: {result}")

main()