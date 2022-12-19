from Engine.print_queue import print_queue
from Windows.dialogue_slate import dialogue_slate


class creation:

    @staticmethod
    def start(screen):

        print_queue.add_event(dialogue_slate)
        dialogue_slate.add("Tester: Just testing here...")
        dialogue_slate.add("test2")

