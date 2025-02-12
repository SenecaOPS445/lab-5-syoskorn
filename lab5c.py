#!/usr/bin/env python3
# Author ID: syoskorn

def add(number1, number2):
    try:
        # Attempt to add the numbers
        result = int(number1) + int(number2)
        return result
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                     # Should work
    print(add('10', 5))                   # Should work
    print(add('abc', 5))                  # Exception handled
    print(read_file('seneca2.txt'))       # Assuming seneca2.txt exists and is accessible
    print(read_file('file10000.txt'))     # Exception handled
