

class player(object):

    # Player Information #

    name = ""
    race = None

    # Player Information #

    # Equipment #

    primary_style = None
    secondary_style = None
    entry_stance = None
    abilities = []
    race_ability = None

    weapon = None
    helmet = None
    chestplate = None
    leggings = None
    boots = None
    enhancer = None

    # Equipment #

    # World Stats #

    world_xp = 0
    WORLD_XP_REQ = 1000
    knowledge_points = 0

    charisma = 0
    wisdom = 0
    empathy = 0
    swimming = 0
    sneaking = 0

    # World Stats #

    # Combat #

    poise = 0
    hp = 0


    # Combat #


    def __init__(self, name, race, charisma, wisdom, observative, swimming, sneaking):
        self.name = name
        self.race = race
        self.charisma = charisma
        self.wisdom = wisdom
        self.observative = observative
        self.swimming = swimming
        self.sneaking = sneaking
