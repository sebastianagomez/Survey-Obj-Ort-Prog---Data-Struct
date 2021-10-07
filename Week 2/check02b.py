# 02 Prepare : Checkpoint B

# Stuent : Sebastian Gomez

# Instructor : Vaughn Poulson

# Write a Python 3 program that reads an input file and counts the number of words and the number of lines in that file.

file = open("c:/Sebi/BYU/Fall 2021/Survey Obj Ort Prog - Data Struct/Week 2/rates.csv", "rt")
data = file.read()
words = data.split()

print(f'The file contains {(len.words)} lines and  words.')


