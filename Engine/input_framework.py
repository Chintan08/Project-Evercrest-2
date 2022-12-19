from Engine.print_queue import print_queue
from Windows.esc_menu import esc_menu


class input_framework:

    @staticmethod
    def ask_number(screen, list_size):

        while True:

            input = screen.getch()

            # ESCAPE LISTENER #
            if input is 27 and print_queue.FLAG_ESCAPE:
                print_queue.add_event(esc_menu)
                break

            if input in range(49, 49+list_size):
                return input-48

    @staticmethod
    def get_key(screen):

        while True:

            input = screen.getch()

            if input == 27 and print_queue.FLAG_ESCAPE:
                print_queue.add_event(esc_menu)
                break

            else:
                break
