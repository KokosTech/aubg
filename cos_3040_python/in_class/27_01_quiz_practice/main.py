# Quiz Prep

"""
Create a python program that asks the user for two numbers 
and prints the result from raising the first to the second.
"""

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print(pow(num1, num2)) # or num1 ** num2

"""
Create a python program that asks the user for one real number 
and then displays the number with 2 symbols after the decimal point, 
on 20 places, aligned in the center.
"""

num = float(input("Enter a real number: "))
print(f"{num:^20.2f}")

"""
Create a python program that asks for three numbers 
and calculates the formula below and displays the result.

a+b / 2c + c^2
"""

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

print((a + b) / 2 * c + pow(c, 2))

"""
Create a python program that asks the user for string and 
then prints only the lowercase letters in the string.
"""

string = input("Enter something: ")
for s in string:
    if s.islower():
        print(s, end='')
        
print()

"""
Create a python program that asks the user for two numbers x and y 
and print the even numbers in the range [x, y].
"""

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

for i in range(x + 1 if x % 2 else x, y + 1, 2):
    print(i)

"""
Create a python program that asks the user to enter an year. 
If entered value is a positive number, check whether it corresponds 
to a leap year and print the result, if not keep asking for a valid year.
"""


while True:
  year = int(input("Enter year: "))

  if year > 0:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      print(f"{year} is a leap year.")
      break
