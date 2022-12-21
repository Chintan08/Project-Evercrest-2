from time import sleep


# Dialogue is a helper method that allows for scrolling text. This is nice for conversations and other outputs.
class dialogue:

    # TODO: color handling

    @staticmethod
    def dia(screen, y, x, content):

        suffix = ""  # Suffixes should not scroll.
        SUFFIX_LIMIT = 10  # The Suffix Limit is how long a suffix can be. Change this if needed.

        for character_index in range(0, len(content)):

            # Identify a suffix if you find one.
            if content[character_index] == ":" and character_index <= SUFFIX_LIMIT:

                for index in range(0, character_index):
                    suffix += content[index]

                screen.addstr(y, x, suffix + ": ")
                break

        BEGIN = 0

        if suffix != "":
            BEGIN = len(suffix) + 2
            x += BEGIN

        # TODO: Adjust sleep timers depending on what punctuation it sees, for punctual impact.
        for character in range(BEGIN, len(content)):

            screen.addstr(y, x, content[character])
            sleep(0.03)
            screen.refresh()
            x += 1
