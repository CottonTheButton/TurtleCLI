#!/usr/local/bin/python3.8
import sys
import turtle

try:
    first_arg = sys.argv[1]

    if first_arg == "corona" or first_arg == "covid":
        print(turtle.corona())

    elif first_arg == "docs":
        turtle.docs(sys.argv[2], sys.argv[3])

    elif first_arg == "factorial":

        try:

            numz = sys.argv[2]
            num = int(numz)

            x = 0
            y = num

            while x < num:
                if y != 1:
                    print(f"{y} * ", end="")
                else:
                    print(y)
                x += 1
                y -= 1

            turtle.factorial(num)

        except IndexError:
            print("Syntax: turtles factorial <number that you want to get that factorial of>")

    elif first_arg == "help":
        commands_list = []

    elif first_arg == "reddit":
        turtle.reddit(sys.argv[2])

    elif first_arg == "ruqqus":
        turtle.ruqqus(sys.argv[2])

    elif first_arg == "talk":
        raise Exception("WIP!!!")

    elif first_arg == "sort":
        turtle.file_alphabetize(sys.argv[2], sys.argv[3])

    elif first_arg == "stocks" or first_arg == "stock":
        turtle.stocks(sys.argv[2])

    else:
        print("What do you want me to do? >__<")


except IndexError:
    print("What do you want me to do? >__<")
