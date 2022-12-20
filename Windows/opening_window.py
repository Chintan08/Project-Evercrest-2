import curses

from Engine.input_framework import input_framework
from Engine.print_queue import print_queue
from Levels.creation import creation
from constants import constants


class opening_window:

    @staticmethod
    def start(screen):

        print_queue.FLAG_ESCAPE = True

        screen.addstr(11, 87, "Welcome to the world of...")
        screen.addstr(13, 59, f"=================================================================================", constants.YELLOW | curses.A_BOLD)

        screen.addstr(15, 59, f" _______           _______  _______  _______  _______  _______  _______ _________", constants.YELLOW | curses.A_BOLD)
        screen.addstr(16, 59, f"(  ____ \|\     /|(  ____ \(  ____ )(  ____ \(  ____ )(  ____ \(  ____ \\__   __/", constants.YELLOW | curses.A_BOLD)
        screen.addstr(17, 59, f"| (    \/| )   ( || (    \/| (    )|| (    \/| (    )|| (    \/| (    \/   ) (   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(18, 59, f"| (__    | |   | || (__    | (____)|| |      | (____)|| (__    | (_____    | |   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(19, 59, f"|  __)   ( (   ) )|  __)   |     __)| |      |     __)|  __)   (_____  )   | |   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(20, 59, f"| (       \ \_/ / | (      | (\ (   | |      | (\ (   | (            ) |   | |   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(21, 59, f"| (____/\  \   /  | (____/\| ) \ \__| (____/\| ) \ \__| (____/\/\____) |   | |   ", constants.YELLOW | curses.A_BOLD)
        screen.addstr(22, 59, f"(_______/   \_/   (_______/|/   \__/(_______/|/   \__/(_______/\_______)   )_(   ", constants.YELLOW | curses.A_BOLD)

        screen.addstr(24, 59, f"=================================================================================", constants.YELLOW | curses.A_BOLD)

        screen.addstr(35, 91, f"1. Start a new game")
        screen.addstr(36, 92, f"2. Load a new game")
        screen.addstr(37, 93, f"3. Quit the game")

    @staticmethod
    def getin(screen):
        input = input_framework.ask_number(screen, 3)

        if input == 1:
            creation.start(screen)
        if input == 2:
            screen.addstr(40, 85, f"You do not have a game to load.", constants.RED)
        if input == 3:
            exit(0)
