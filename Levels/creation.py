from time import sleep

from Engine.input_framework import input_framework
from Engine.print_queue import print_queue
from Windows.dialogue_slate import dialogue_slate
from Windows.question_slate import question_slate
from colors import colors
from constants import constants


class creation:

    @staticmethod
    def start(screen):

        slate = dialogue_slate()
        print_queue.add_event(slate)
        slate.add(f"Tester: Just testing here...")
        slate.add("test2")

        ask = question_slate("How are you?", ["lol", ";(", "ok"])
        print_queue.add_event(ask)
        answer = ask.get_last_input()

        if answer == 0:
            print_queue.add_previous()

        else:

            slate = dialogue_slate()
            print_queue.add_event(slate)
            slate.add(f"Tester: yoikes...")
            slate.add(f"test{ask.last_input}")