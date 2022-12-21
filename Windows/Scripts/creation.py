from Engine.print_queue import print_queue
from Windows.Slates.dialogue_slate import dialogue_slate
from Windows.Slates.question_slate import question_slate


class creation:

    phase = 0
    FLAG_ANSWER = True

    @staticmethod
    def run(screen):

        if creation.phase == 0:
            slate = dialogue_slate()
            print_queue.add_event(slate)
            slate.add(f"Tester: Just testing here...")
            slate.add("test2")

            creation.phase += 1

        elif creation.phase == 1:
            ask = question_slate("How are you?", ["lol", ";(", "ok"])
            print_queue.add_event(ask)
            creation.phase += 1

        elif creation.phase == 2:

            answer = print_queue.get_last_input()

            if answer == 0:
                print_queue.add_previous()

            else:

                slate = dialogue_slate()
                print_queue.add_event(slate)
                slate.add(f"Tester: yoikes...")
                slate.add(f"test{answer}")

                creation.FLAG_ANSWER = False

