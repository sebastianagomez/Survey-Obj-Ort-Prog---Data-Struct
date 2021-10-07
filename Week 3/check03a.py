""" 
03 Prepare : Checkpoint A

Stuent : Sebastian Gomez

Instructor : Vaughn Poulson

Write a Python 3 program according to the following:

- Create a class for a Student, that contains a first name, a last name, and an id.

- Create an __init__ function in your class that initializes the first name, last name, and id to "", "", and 0, respectively.

- Create a regular function (not a member function just yet) called prompt_student that creates a new student object, then prompts the user for a first name, 
last name, and id. The function should assign these to the appropriate properties of the object and return it.

- Create a regular function (not a member function) called display_student that accepts a student object, and displays its information in the following format: "id - 
FirstName LastName".

- Then, create a main function that does the following:

- Calls the prompt_student function and saves the returned value in a variable called "user".

- Pass the user object to the display_student function to be displayed.
"""

def prompt_user():
    student = Student()
    student.first_name = input("Please enter your first name: ")
    student.surename = input("Please enter your last name: ")
    student.student_id = int(input("Please enter your id number: "))
    return student

class Student:

    def __init__(self):
        self.first_name = ""
        self.surename = ""
        self.student_id = ""

def display_student(my_student):
    print()
    print("Your information:")
    print(f"{my_student.student_id} - {my_student.first_name} {my_student.surename}")

def main():
    person = prompt_user()
    display_student(person)

if __name__ == '__main__':
    main()