from Engine.input_framework import input_framework
from Engine.print_queue import print_queue
from Engine.dialogue import dialogue
from Engine.constants import constants


class dialogue_slate:

    strlist = []

    def __init__(self):
        self.strlist = []

    def start(self, screen):

        print_queue.FLAG_ESCAPE = False

        y = 0
        for string in self.strlist:
            dialogue.dia(screen, y, 0, string)
            y += 2
            self.getenter(screen)
            if y >= 15:
                screen.clear()

    def getenter(self, screen):

        screen.addstr(constants.TERMINAL_Y-1, int(screen.getmaxyx()[1]/2) - 10, "Press any key to continue")
        input_framework.get_key(screen)
        screen.addstr(constants.TERMINAL_Y-1, int(constants.TERMINAL_X/2) - 10, "                         ")

    # Important Note:
    # Screens that need to handle inputs in-house to continue building do NOT use getin()
    # Instead, they should do it themselves. The Print Queue is the only thing that uses getin().
    @staticmethod
    def getin(screen):
        pass

    def add(self, string):
        self.strlist.append(string)
