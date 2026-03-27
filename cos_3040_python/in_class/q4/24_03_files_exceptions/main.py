# EX 01

from pathlib import Path

print("============= EX 01 =================")

try: 
    lst = [10, 20, 30, 40]
    idx = int(input("Enter an index: "))
    print(lst[idx])
except ValueError:
    print("Invalid input. Please enter an integer.")
except IndexError:
    print("Index out of range. Please enter a valid index.")
else:
    print("Value retrieved successfully.")
finally:
    print("Done accessing list")

# EX 07
print("============= EX 07 =================")

filename = input("Enter the filename: ")

path = Path(filename)

try:
    with path.open('r') as file:
        countLines = 0
        countChars = 0
        countCharsNoSpaces = 0
        
        for line in file:
            countLines += 1
            countChars += len(line)
            countCharsNoSpaces += len(line.replace(" ", ""))
        
        print(f"Lines: {countLines}")
        print(f"Characters: {countChars}")
        print(f"Characters (excluding spaces): {countCharsNoSpaces}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    
