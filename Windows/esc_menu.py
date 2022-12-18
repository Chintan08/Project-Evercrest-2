import curses

class esc_menu:

    menu_win = ""

    @staticmethod
    def start(screen):

        esc_menu.menu_win = curses.newwin(screen.getmaxyx()[0], screen.getmaxyx()[1])

        esc_menu.menu_win.addstr(50, 50, "resume 1 exit 2")

    @staticmethod
    def getin(screen):

        while True:

            input = screen.getch()

            if input in range(49, 51):
                if input is 49:
                    esc_menu.menu_win.clear()
                    break

                if input is 50:
                    exit(0)