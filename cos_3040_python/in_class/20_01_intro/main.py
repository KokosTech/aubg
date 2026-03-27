# exe 1

stud_name = "John Doe"
stud_id = 200_201_606

print(f"{stud_id:^10} {stud_name:^20}")
print("{0:^10} {1:^20}".format(stud_id, stud_name))

# exe 2

var = int(input("Enter one integer: "))
var2 = int(input("Enter second integer: "))

print(f"{var} // {var2} = {var / var2}")
print(isinstance(var / var2, int))
