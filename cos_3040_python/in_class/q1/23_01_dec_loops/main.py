# Conditions
# Exe 01

num = int(input("Enter an integer: "))

if num > 0:
  print("Number is positive")
elif num:
  print("Number is negative")
else:
  print("Number is zero")
  
print(f"Number is {"odd" if num % 2 else "even"}")

# Exe 02

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

if any([height <= 0, weight <= 0]):
  print("Please enter valid values")
  exit

bmi = round(weight / pow(height, 2), 2)

print(f"Your BMI is {bmi}", end=' ')

if bmi < 18.5: 
  print("underweight")
elif bmi < 25.0:
  print("normal weight")
elif bmi < 30.0:
  print("overweight")
else:
  print("obese")

# Loops
# Exe 01

i = 10

while i > 0:
  print(i)
  i -= 1
else:
  print("done")
  
# Exe 02

lower = int(input("Enter a lower bound: "))
upper = int(input("Enter an upper bound: "))
step = int(input("Enter step: "))

for i in range(lower, upper + 1, step):
  print(i)
else:
  print("done")

# Exe 03

sum = 0
while True:
  num = int(input("Enter an integer to sum: "))
  
  if not num:
    break
  
  sum += num
  print(sum)

# Exe 04

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(
    f"The triangle can{"" if a == b and b != c else "'t"} be an isosceles triangle")
    
# Exe 05

sen = input("Enter something: ")

for i in sen:
  print(i)

# Exe 06

i = 1
while pow(i, 2) < 50:
  print(pow(i, 2))
  i += 1