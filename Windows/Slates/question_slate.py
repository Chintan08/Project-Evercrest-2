from time import sleep

from Engine.constants import constants
from Engine.input_framework import input_framework
from Engine.game import game


class question_slate:

    question = ""
    response = []

    def __init__(self, question, response):
        self.question = question
        self.response = response
        self.last_input = 0

    def start(self, screen):

        game.FLAG_ESCAPE = False

        screen.addstr(0, 0, self.question)
        screen.move(2, 0)
        for index in range(0, len(self.response)):
            screen.addstr(f"{index+1}. " + self.response[index] + "\n")

        screen.addstr(constants.TERMINAL_Y-1, int(screen.getmaxyx()[1]/2) - 7, "What do you do?")

    def getin(self, screen):

        return input_framework.ask_number(screen, len(self.response))

