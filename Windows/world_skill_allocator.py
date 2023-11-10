import curses

from Engine.constants import constants
from Engine.input_framework import input_framework
from Engine.game import game


class world_skill_allocator:

    total_points = 10
    charisma = 0

    @staticmethod
    def start(screen):

        game.FLAG_ESCAPE = False

        screen.addstr(3, int(constants.TERMINAL_X/2) - 34, "Question 3: Allocate 10 points into these 6 characteristics to define yourself.")

        screen.addstr(6, 5, f"Charisma: {world_skill_allocator.charisma}")
        screen.addstr(7, 5, f"Wisdom: ")
        screen.addstr(8, 5, f"Empathy: ")

        win = curses.newwin(20, 32, constants.CENTER_Y-10, constants.TERMINAL_X - 50)
        win.border()
        win.addstr(4, 10, "Total Points", curses.A_BOLD)
        win.addstr(int(win.getmaxyx()[0]/2), 15, f"{world_skill_allocator.total_points}")

        win.overlay(screen)

    @staticmethod
    def getin(screen):

        input = input_framework.ask_number(screen, 3)

    @staticmethod
    def get_points():
        pass