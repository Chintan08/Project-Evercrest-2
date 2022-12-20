from time import sleep

from Engine.input_framework import input_framework
from Engine.print_queue import print_queue


class question_slate:

    question = ""
    response = []
    last_input = 0

    def __init__(self, question, response):
        self.question = question
        self.response = response
        self.last_input = 0

    def start(self, screen):

        print_queue.FLAG_ESCAPE = True

        screen.addstr(0, 0, self.question)
        y = 2
        for index in range(0, len(self.response)):
            screen.addstr(y, 0, f"{index+1}. " + self.response[index])
            y += 1

        screen.addstr(y + 2, 0, "What do you do?")

    def getin(self, screen):

        self.set_last_input(input_framework.ask_number(screen, len(self.response)))
        screen.addstr(10, 10, f"{self.last_input}")
        screen.refresh()
        sleep(1)

    def set_last_input(self, input):
        self.last_input = input

    def get_last_input(self):
        return self.last_input


