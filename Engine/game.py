

# Game is a game loop that draws screens onto the terminal and looks to gain inputs
# Games usually do updates before drawing, but terminal games need to do this in reverse.
# The Print Queue stores vital information including current scripts, last inputs, and a list of old screens that have passed through program run.
class game:

    # The queue is a list of print events. The first event to go is located at the head.
    queue = []

    # A list of every old screen to exist.
    # TODO: This can memory leak with enough game time. Find a way to prune this list when necessary.
    old_screens = []

    # The current screen to be drawn and receive inputs from.
    print_event = None

    # The current script is the class that builds windows and reacts to them. Usually classes that need to use slates. Current scripts are added by static screens usually.
    current_script = None

    # If true, Escape can lead to a menu. Windows set this. Input handlers set action to this.
    FLAG_ESCAPE = True

    # If true, we will not respond to the current_script.
    FLAG_COMBAT = False

    # Stores getin()'s last received input. Used for current scripts.
    last_received_input = 0

    # The main game loop is here, called from main
    @staticmethod
    def start(screen):

        # Clear terminal screen on launch
        screen.clear()

        # GAME LOOP #
        while True:

            # When there is something in the queue, pull it as the print event
            # We give the screen to old_screens, then delete the entry in the queue.
            # Because a gap is left in the queue, we ask to rebuild the queue to make sure it is not broken.
            # Clear the previous screen then continue operations.
            if len(game.queue) is not 0:
                game.print_event = game.queue[0]
                game.old_screens.append(game.print_event)
                del game.queue[0]
                game.rebuild()
                screen.clear()

            # All print events have a start method. Displays what the print event wants to.
            game.print_event.start(screen)

            screen.refresh()

            # Store the input returned from getin(). getin() HAS to return a value unless it is an exit.
            game.last_received_input = game.print_event.getin(screen)

            # Check if we can talk to current script.
            if game.current_script is not None and game.current_script.FLAG_ANSWER and not game.FLAG_COMBAT:
                game.current_script.run(screen)  # We let the current script change phases because it wants full control of it.

            # Check if current script needs to be removed.
            if game.current_script is not None and game.current_script.FLAG_ANSWER is False:
                game.current_script = None

            screen.refresh()

    # Adds a print event to the queue.
    @staticmethod
    def add_event(event):
        game.queue.append(event)

    # Adds a previous screen to the queue.
    # Can lead to an index out of bounds error, but should not be possible as a minimum of 2 screens had to have existed before this is ever called.
    @staticmethod
    def add_previous():
        game.add_event(game.old_screens[len(game.old_screens) - 2])

    # Sets the current script. Called from static screens like opening_screen or a location screen.
    @staticmethod
    def set_script(script):
        game.current_script = script

    # Returns previous input.
    @staticmethod
    def get_last_input():
        return game.last_received_input

    # Rebuilds the queue by building a new queue and swapping them.
    # Rebuilds, as of 12/20/2022, have no real purpose. Because the queue only ever expects 1 entry, there is never a hole.
    @staticmethod
    def rebuild():

        temporary = []
        for item in game.queue:
            if item is not None:
                temporary.append(item)

        game.queue = temporary
