import json


def ex3():
    with open('data.json') as f:
        data = json.load(f)
        total = 0
        for employee in data['employees']:
            print(f"Name: {employee['name']}, Salary: {employee['salary']}")
            total += employee['salary']

        print(f"Total salary: {total}")

        print("Adding a new employee...")
        data['employees'].append({"name": "Charlie", "salary": 2000})

        with open('data_new.json', 'w') as f:
            json.dump(data, f, indent=2)


def magic(op1, op2, operation):
    try:
        if operation == '/':
            return op1 / op2
        else:
            return op1 + op2
    except ZeroDivisionError:
        return 0
    except Exception:
        raise

# Given the following function create unit tests to cover all cases:

from unittest import TestCase, main


class TestMagic(TestCase):
    def test_magic_div(self):
        self.assertEqual(magic(10, 2, '/'), 5)
    
    def test_magic_add(self):
        self.assertEqual(magic(10, 2, '+'), 12)
        
    def test_magic_div_zero(self):
        self.assertEqual(magic(10, 0, '/'), 0)
    
    def test_magic_invalid_operation(self):
        with self.assertRaises(Exception):
            magic(10, 2, '*')
