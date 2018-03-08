"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    userinput = raw_input().split(" ")
    try:
        if userinput[0] == "q":
            break
        else:
            try:
                num1 = float(userinput[1])
                if userinput[0] == 'square':
                    print square(num1)
                elif userinput[0] == 'cube':
                    print cube(num1)
                else:
                    try:
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
                    except ValueError:
                        print "Your third input was invalid. Please try again"

            except ValueError:
                print "Your second input was invalid. Please try again"

    except IndexError or ValueError:
        print "Your first input was invalid. Please try again"
