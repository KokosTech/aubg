import re


def ex1():
    test_cases = ['200275606', '200275606a', '200275607']
    
    pat = re.compile(r'^[0-9]{9}$')
    
    for test in test_cases:
        print(f"Testing {test=} {pat.search(test).group()=}")
    
    
def parse_row(row):
    parts = row.split(';')
    if len(parts) != 3:
        raise ValueError("Invalid row format")
    
    if not re.match(r'^[0-9]{9}$', parts[0]):
        raise ValueError("Incorrect student id number")
    
    if not re.match(r'^[A-Za-z]* [A-Za-z]*$', parts[1]):
        raise ValueError("Invalid student name")
    
    if not re.match(r'^[0-9]{1,3}\.*[0-9]+$', parts[2]):
        raise ValueError("Invalid grade")
    
    return row


def parse_row_new(row):
    parts = row.split(';')
    if len(parts) != 3:
        raise ValueError("Invalid row format")

    if not re.match(r'^[0-9]+$', parts[0]):
        raise ValueError("Incorrect student id number")

    if not re.match(r'^([A-Z]+[a-z]+\s)+$', parts[1]):
        raise ValueError("Invalid student name")

    if not re.match(r'^100.0|[1-9]?[0-9](.[0-9])$', parts[2]):
        raise ValueError("Invalid grade")

    return row
    
def ex02():
    with open('stud.csv', 'r') as f:
        for line in f:
            parse_row_new(line.strip())
            
    
if __name__ == "__main__":
    # ex1()
    ex02()
