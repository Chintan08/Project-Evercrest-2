import curses
from time import sleep

from Engine.input_framework import input_framework
from Engine.game import game


class open_slate:

    question = ""

    def __init__(self, question):
        self.question = question

    def start(self, screen):

        game.FLAG_ESCAPE = False

        screen.addstr(0, 0, self.question)

        screen.addstr(1, 0, "Press ENTER to finish your entry. Your entry cannot be empty.")

    def getin(self, screen):

        character = ""
        string = ""

        curses.curs_set(True)
        screen.move(4, 0)

        while True:
            character = screen.getch()

            if character is 10 and len(string) > 0:
                break

            if character is 8 and len(string) > 0:

                string = string[0:len(string)-1]

                screen.clear()
                self.start(screen)
                screen.move(4, 0)

            else:
                string += ""+chr(character)

            screen.addstr(4, 0, string)

        curses.curs_set(False)
        return string.strip()

