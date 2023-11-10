from Engine.game import game
from Windows.esc_menu import esc_menu


# A helper class that gets inputs and returns them after reducing the received character into a real number (1, 2, 3, etc.).
# Input Framework listens for the Escape key press. They are capable of pushing screens like the escape menu.
# Escape menus can only appear if the print queue's FLAG_ESCAPE is true. This is set by screens.
class input_framework:

    # Ask Number returns a number in the possible range of answers, determined by list_size.
    @staticmethod
    def ask_number(screen, list_size):

        while True:

            input = screen.getch()

            if input is 27 and game.FLAG_ESCAPE:
                game.add_event(esc_menu)
                break

            if input in range(49, 49+list_size):
                return input-48

    # Get Key is used by dialogue slates to buffer between dialogue.
    # It listens for escape if possible.
    # Because it is listening for any key, it does not need to return the key, and instead breaks from its loop.
    @staticmethod
    def get_key(screen):

        while True:

            input = screen.getch()

            if input == 27 and game.FLAG_ESCAPE:
                game.add_event(esc_menu)
                break

            else:
                break
