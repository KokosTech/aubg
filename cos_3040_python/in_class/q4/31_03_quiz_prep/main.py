# Task 1

import re


def task01():
    try:
        with open("some.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line.replace(" ", ""))
    except FileNotFoundError:
        print("The file some.txt was not found.")

# Task 2

def task02():
    try:
        with open("some2.txt", "w") as f:
            number = 0
            while number != "":
                number = input("Enter a number: ")
                check = re.match(r"^-?\d+(\.\d{1,6})?$", number)
                if check:
                    f.write(number + "\n")
                else:
                    print("Invalid input. Please enter a valid number.")
    except IOError:
        print("An error occurred while writing to the file.")    
    
# Task 3


def task03():
    try:
        with open("trans.txt", 'r') as f:
            balance = 0.0
            
            for i, line in enumerate(f.readlines()):
                line = line.strip()
                check = re.match(r"^[cd|CD][\s\t]\d+(\.\d{1,6})?$", line)
                
                if check:
                    opcode = line.split()[0].lower()
                    sum = float(line.split()[1])
                    
                    if opcode == 'c':
                        balance -= sum
                    elif opcode == 'd':
                        balance += sum
                else:
                    raise ValueError(f"Wrong information on line {i + 1}: {line}")
                        
    except FileNotFoundError:
        print("File does not exist...")
    except ValueError as ve:
        print(ve)

def task04():
    try:
        with open("random.txt", 'r'):
            ...
    except FileNotFoundError:
        print("File does not exist...")
