from Engine.game import game
from Races.arc import arc
from Races.galed import galed
from Windows.Slates.dialogue_slate import dialogue_slate
from Windows.Slates.open_slate import open_slate
from Windows.Slates.question_slate import question_slate
from Windows.world_skill_allocator import world_skill_allocator


class creation:

    phase = 3
    FLAG_ANSWER = True

    @staticmethod
    def run(screen):

        name = ""
        race = None

        if creation.phase == 0:
            slate = dialogue_slate()
            game.add_event(slate)
            slate.add(f"???: Hello everyone!")
            slate.add("???: Welcome to the Mercenary Bootcamp! I am Tracey, the lead of this bootcamp.")
            slate.add("Tracey: You all are here for an important reason; to become mercenaries of the great land of Evercrest!")
            slate.add("Tracey: Now, I'm sure you know why you want to be a mercenary. Killing monsters, collecting bounties, and getting money is an exciting life!")
            slate.add("Tracey: But, before you can do any of those things, you have to be licensed. That is where we come in.")
            slate.add("Tracey looks around. There were no other people in the small building but the fifteen mercenaries.")
            slate.add("Tracey: We, as in just I. But that's okay! All I ask from you is that you fill out this questionnaire, so we can get started. I hope you can read!")

            creation.phase += 1

        elif creation.phase == 1:
            name = open_slate("Question 1: What is your name?")
            game.add_event(name)
            creation.phase += 1

        elif creation.phase == 2:

            race = question_slate("Question 2: What is your race?", [f"{arc.name}: \n{arc.creation_description}\n",
                                                                     f"{galed.name}: \n{galed.creation_description}\n"])
            game.add_event(race)

            creation.phase += 1

        elif creation.phase == 3:

            game.add_event(world_skill_allocator)
            creation.phase += 1

        elif creation.phase == 4:

            points = world_skill_allocator.get_points()


