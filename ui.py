""" user interface module """
import os
import sys
import time
from collections import OrderedDict

import termcolor

CLEAR_SCREEN = True
PRINT_SPEED = 0
COLOR = True


def delayed_print(text, color=None):
    """ prints characters with delay provided between each character. color for prompt is optional """

    # iterate over every character in string one by one
    for char in str(text):
        # only print color if a color is indicated and color is allowed
        if color and COLOR:
            sys.stdout.write(termcolor.colored(char, color))
        else:
            sys.stdout.write(char)

        sys.stdout.flush()

        # delay the loop to show the appearence of text rolling out on screen
        time.sleep(PRINT_SPEED)


def accepted_input(*accepted):
    """ ensures user provides input that is accepted """

    # unpack the accepted parameter
    accepted = [str(s) for s in accepted]

    # show the input prompt to the screen
    choice = input("\n>> ")

    # loop infinitely until a valid input is entired
    while choice not in accepted:
        remove_lines(1)
        print("Invalid! >> ", "red")
        choice = input()

    return choice


def prompt(message, function=None, *args):
    """ prompts user with y/n. if function is provided and the users answers y, the function will be executed"""

    print(str(message) + " [y/n]:")
    choice = accepted_input("y", "n")

    # ensure there is a function to execute
    if function and choice == "y":
        # unpack parameter and execute the function
        function(*args)

    if choice == "n":
        return False

    return True


def clr():
    """ clears the terminal """
    if CLEAR_SCREEN:
        # clear the screen based on the operating system
        os.system("cls" if os.name=="nt" else "clear")


def remove_lines(amount):
    """ deletes lines printed previously """

    # character codes to cursor up and erase a line
    cursor_up = "\x1b[1A"
    erase = "\x1b[2K"

    # iterate however many line deletions are requested
    for _ in range(amount):
        sys.stdout.write(cursor_up)
        sys.stdout.write(erase)


class Menu(object):
    """ displays a numbered menu with optional prompt. if an item is selected, the function corresponding to that item will be executed """

    def __init__(self, header=None):
        self.header = header
        self.options = OrderedDict()

    def add(self, description, route="", *args):
        """ adds an option to the menu. """

        option_number = len(self.options) + 1 # menus start at 1
        # option display format:
        #         option number
        #         description (calls 'route' which is a function)
        self.options.update({str(option_number): [str(description), route, args]})

    def display(self, menu_prompt=True):
        """ displays all options in a menu """

        clr()
        print(self.header + "\n")
        print("-----------------\n")

        # display the options
        for option_number, description in self.options.items():
            print("{}) {}\n".format(option_number, description[0]))

        if menu_prompt:
            # continue to pester user until a valid choice is selected
            choice = self.options.get(input("\n>> "))
            while not choice:
                remove_lines(1)
                print("Invalid! >> ", "red")
                choice = self.options.get(input())

            if choice[1]:
                # function address and args
                choice[1](*choice[2])

            self.exit()

        return

    def exit(self):
        """ ask user if they want to quit """

        if not prompt("\nReturn back to menu?", None):
            raise SystemExit

        self.display()
