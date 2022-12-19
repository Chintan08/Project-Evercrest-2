import curses

from Engine.print_queue import print_queue
from constants import constants


class esc_menu:

    win = ""

    @staticmethod
    def start(screen):

        esc_menu.win = curses.newwin(30, 60, int(constants.TERMINAL_Y/2)-15, int(constants.TERMINAL_X/2)-30)
        esc_menu.win.attron(constants.YELLOW)
        esc_menu.win.border()

        esc_menu.win.addstr(int((esc_menu.win.getmaxyx()[0]/2)-10), int(esc_menu.win.getmaxyx()[1]/2)-4, "Main Menu", curses.A_BOLD | constants.RED)
        esc_menu.win.addstr(int((esc_menu.win.getmaxyx()[0] / 2) - 3), int(esc_menu.win.getmaxyx()[1] / 2) - 8,
                            "1. Resume to game")
        esc_menu.win.addstr(int((esc_menu.win.getmaxyx()[0] / 2) - 1), int(esc_menu.win.getmaxyx()[1] / 2) - 8,
                            "2. Save your game")
        esc_menu.win.addstr(int((esc_menu.win.getmaxyx()[0] / 2) + 1), int(esc_menu.win.getmaxyx()[1] / 2) - 9,
                            "3. Exit to desktop")

        esc_menu.win.overlay(screen)

    @staticmethod
    def getin(screen):

        while True:

            input = screen.getch()

            if input in range(49, 52):
                if input is 49:
                    print_queue.add_previous()
                    break

                if input is 50:
                    esc_menu.win.addstr(int((esc_menu.win.getmaxyx()[0] / 2)) + 5, int(esc_menu.win.getmaxyx()[1] / 2) - 12, "Your game has been saved.")
                    esc_menu.win.refresh()  # Important note: Windows need to be refreshed by the window itself, not by the print queue.

                if input is 51:
                    exit(0)
