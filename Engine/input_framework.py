from Engine.print_queue import print_queue
from Windows.esc_menu import esc_menu


class input_framework:

    @staticmethod
    def ask_number(screen, list_size):

        while True:

            input = screen.getch()

            # ESCAPE LISTENER #
            if input is 27:
                print_queue.add_event(esc_menu)

            if input in range(49, 49+list_size):
                return input-48
