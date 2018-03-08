"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    userinput = raw_input().split(" ")

    if userinput[0] == "q":
        break
    else:
        num1 = float(userinput[1])
        if userinput[0] == 'square':
            print square(num1)
        elif userinput[0] == 'cube':
            print cube(num1)
        else:
            num2 = float(userinput[2])

            if userinput[0] == "+":
                print add(num1, num2)
            elif userinput[0] == '-':
                print subtract(num1, num2)
            elif userinput[0] == '*':
                print multiply(num1, num2)
            elif userinput[0] == '/':
                print divide(num1, num2)
            elif userinput[0] == 'pow':
                print power(num1, num2)
            elif userinput[0] == 'mod':
                print mod(num1, num2)
