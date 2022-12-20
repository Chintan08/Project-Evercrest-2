from time import sleep


class dialogue:

    # TODO: color handling

    @staticmethod
    def dia(screen, y, x, content):

        suffix = ""
        SUFFIX_LIMIT = 10

        for character_index in range(0, len(content)):

            if content[character_index] == ":" and character_index <= SUFFIX_LIMIT:

                for index in range(0, character_index):
                    suffix += content[index]

                screen.addstr(y, x, suffix + ": ")
                break

        BEGIN = 0

        if suffix != "":
            BEGIN = len(suffix) + 2
            x += BEGIN

        for character in range(BEGIN, len(content)):

            screen.addstr(y, x, content[character])
            sleep(0.03)
            screen.refresh()
            x += 1
