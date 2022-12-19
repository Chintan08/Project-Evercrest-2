import curses

from Engine.input_framework import input_framework
from Engine.print_queue import print_queue
from Engine.dialogue import dialogue
from constants import constants


class dialogue_slate:

    win = ""
    strlist = []

    @staticmethod
    def start(screen):

        print_queue.FLAG_ESCAPE = False

        y = 0
        for string in dialogue_slate.strlist:
            dialogue.dia(screen, y, 0, string)
            y += 2
            dialogue_slate.getenter(screen)

    @staticmethod
    def getenter(screen):

        screen.addstr(constants.TERMINAL_Y-1, int(screen.getmaxyx()[1]/2) - 10, "Press any key to continue")
        input_framework.get_key(screen)

    @staticmethod
    def getin(screen):
        pass

    @staticmethod
    def add(string):
        dialogue_slate.strlist.append(string)
