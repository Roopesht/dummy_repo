# Test: 
# 1. Run this file,
# 2. call the function 
# 3. Verify if the numbers from 1..<number> is printed

# Create a new file print_num.py
# create a function print_num
# function accepts a number, and print numbers 1..

def print_num(number):
    for i in range(1, number+1):
        print(i)

print_num(10)

