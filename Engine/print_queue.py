

class print_queue:

    queue = []
    old_screen = []
    screen_index = 0

    # If true, Escape can lead to a menu. Windows set this. Input handlers set action to this.
    FLAG_ESCAPE = True

    @staticmethod
    def start(screen):

        screen.clear()

        # the print queue is the whole game.
        # you only start the loop once, so we can print the main menu once.
        print_event = print_queue.queue[0]

        # game loop
        while True:

            if len(print_queue.queue) is not 0:
                print_event = print_queue.queue[len(print_queue.queue)-1]
                print_queue.old_screen.append(print_event)
                print_queue.screen_index = len(print_queue.old_screen)-1
                del print_queue.queue[len(print_queue.queue)-1]
                screen.clear()

            screen.refresh()
            print_event.start(screen)
            print_event.getin(screen)
            screen.refresh()

    @staticmethod
    def add_event(event):

        if len(print_queue.queue) == 0:
            print_queue.queue.append(event)

        else:

            for i in range(len(print_queue.queue))[::-1]:
                if i is 0:
                    print_queue.queue[i] = event
                    break

                else:
                    print_queue.queue[i+1] = i

    @staticmethod
    def add_previous():
        print_queue.add_event(print_queue.old_screen[print_queue.screen_index-1])
