

class print_queue:

    queue = []

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
                del print_queue.queue[len(print_queue.queue)-1]
                screen.clear()

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
