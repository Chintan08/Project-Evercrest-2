import curses

from Engine.input_framework import input_framework
from Engine.game import game
from Windows.Scripts.creation import creation
from Engine.constants import constants


class test_kingdom:

    @staticmethod
    def start(screen):

        game.FLAG_ESCAPE = True
        screen.addstr(f"{screen.getmaxyx()[0]}\n")
        screen.addstr(f"{screen.getmaxyx()[1]}")

        X_POS = int(constants.TERMINAL_X/2) - int(48/2)

        screen.addstr(12, X_POS, f" __      __     _         _                     ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(13, X_POS, f" \ \    / /    | |       | |                    ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(14, X_POS, f"  \ \  / /__ _ | |  __ _ | |_  ___  _ __    ___ ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(15, X_POS, f"   \ \/ // _` || | / _` || __|/ _ \| '_ \  / _ \\", constants.YELLOW | curses.A_BOLD)
        screen.addstr(16, X_POS, f"    \  /| (_| || || (_| || |_|  __/| | | ||  __/", constants.YELLOW | curses.A_BOLD)
        screen.addstr(17, X_POS, f"     \/  \__,_||_| \__,_| \__|\___||_| |_| \___|", constants.YELLOW | curses.A_BOLD)


    @staticmethod
    def getin(screen):

        input = input_framework.ask_number(screen, 3)

        if input == 1:
            game.set_script(creation)
            return input

        if input == 2:
            screen.addstr(40, 85, f"You do not have a game to load.", constants.RED)
            return input

        if input == 3:
            exit(0)
