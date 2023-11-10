import curses

from Engine.input_framework import input_framework
from Engine.game import game
from Windows.Scripts.creation import creation
from Engine.constants import constants
from Windows.test_kingdom import test_kingdom


class opening_window:

    @staticmethod
    def start(screen):

        game.FLAG_ESCAPE = False
        screen.addstr(f"{screen.getmaxyx()[0]}\n")
        screen.addstr(f"{screen.getmaxyx()[1]}")

        X_POS = int(constants.TERMINAL_X / 2) - int(81 / 2)
        X_GENERAL = int(constants.TERMINAL_X / 2)

        screen.addstr(11, X_GENERAL - 13, "Welcome to the world of...")
        screen.addstr(13, X_POS, f"=================================================================================", constants.YELLOW | curses.A_BOLD)

        screen.addstr(15, X_POS, f" _______           _______  _______  _______  _______  _______  _______ _________", constants.YELLOW | curses.A_BOLD)
        screen.addstr(16, X_POS, f"(  ____ \|\     /|(  ____ \(  ____ )(  ____ \(  ____ )(  ____ \(  ____ \\__   __/", constants.YELLOW | curses.A_BOLD)
        screen.addstr(17, X_POS, f"| (    \/| )   ( || (    \/| (    )|| (    \/| (    )|| (    \/| (    \/   ) (   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(18, X_POS, f"| (__    | |   | || (__    | (____)|| |      | (____)|| (__    | (_____    | |   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(19, X_POS, f"|  __)   ( (   ) )|  __)   |     __)| |      |     __)|  __)   (_____  )   | |   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(20, X_POS, f"| (       \ \_/ / | (      | (\ (   | |      | (\ (   | (            ) |   | |   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(21, X_POS, f"| (____/\  \   /  | (____/\| ) \ \__| (____/\| ) \ \__| (____/\/\____) |   | |   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(22, X_POS, f"(_______/   \_/   (_______/|/   \__/(_______/|/   \__/(_______/\_______)   )_(   ", constants.YELLOW | curses.A_BOLD)

        screen.addstr(24, X_POS, f"=================================================================================", constants.YELLOW | curses.A_BOLD)

        screen.addstr(35, X_GENERAL - 9, f"1. Start a new game")
        screen.addstr(36, X_GENERAL - 9, f"2. Load a new game")
        screen.addstr(37, X_GENERAL - 8, f"3. Quit the game")

    @staticmethod
    def getin(screen):

        input = input_framework.ask_number(screen, 3)

        if input == 1:
            # game.set_script(creation)
            game.add_event(test_kingdom)
            return input

        if input == 2:
            screen.addstr(40, 85, f"You do not have a game to load.", constants.RED)
            return input

        if input == 3:
            exit(0)
