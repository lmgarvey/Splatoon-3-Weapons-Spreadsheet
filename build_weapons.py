# L.M. Garvey, 2023

# helper file for main.py to build the weapon dictionaries
# this is ostensibly to keep the main file cleaner, and not clutter it up
#       with 100+ weapon initializations

# for each class, the associated function will set up a dictionary of the form:
#   {   spec A: ( name of class specific A, offset from first spec A column as 0-3 )
#       spec B: ( name of class specific B, offset from first spec B column as 0-3 )
#       weapon name:
#         {
#         sub: name of sub
#         special: name of special
#         points: current freshness points, defaulted to zero
#         range: range out of 100
#         role: role(s)
#         weight: light, middle, or heavy
#         class_specific_A: value out of 100
#         class_specific_B: value out of 100
#         special points: points needed for special
#         }
#     }
# class_specific_A and _B are the two values that change based on the class
# these types will be listed in the corresponding function docstring


def build_blasters() -> dict:
    """
    Creates the blaster dictionary
    class specifics: impact, fire rate
    :return: the blaster dictionary
    """

    blasters = ["blaster", "clash blaster", "clash blaster neo", "custom blaster", "luna blaster",
                "luna blaster neo", "range blaster", "rapid blaster", "rapid blaster deco",
                "rapid blaster pro", "rapid blaster pro deco", "s-blast '91", "s-blast '92"]

    blaster_dct = dict()
    for blaster in blasters:
        blaster_dct[blaster] = dict()

    blaster_dct["spec A"] = ("impact", 0)
    blaster_dct["spec B"] = ("fire rate", 0)

    blaster_dct["blaster"]["sub"] = "autobomb"
    blaster_dct["blaster"]["special"] = "big bubbler"
    blaster_dct["blaster"]["points"] = 0
    blaster_dct["blaster"]["range"] = 27
    blaster_dct["blaster"]["role"] = "slayer"
    blaster_dct["blaster"]["weight"] = "middle"
    blaster_dct["blaster"]["impact"] = 70
    blaster_dct["blaster"]["fire rate"] = 20
    blaster_dct["blaster"]["special points"] = 180

    blaster_dct["clash blaster"]["sub"] = "splat bomb"
    blaster_dct["clash blaster"]["special"] = "trizooka"
    blaster_dct["clash blaster"]["points"] = 0
    blaster_dct["clash blaster"]["range"] = 21
    blaster_dct["clash blaster"]["role"] = "skirmisher, slayer"
    blaster_dct["clash blaster"]["weight"] = "light"
    blaster_dct["clash blaster"]["impact"] = 30
    blaster_dct["clash blaster"]["fire rate"] = 65
    blaster_dct["clash blaster"]["special points"] = 180

    blaster_dct["clash blaster neo"]["sub"] = "curling bomb"
    blaster_dct["clash blaster neo"]["special"] = "super chump"
    blaster_dct["clash blaster neo"]["points"] = 0
    blaster_dct["clash blaster neo"]["range"] = 21
    blaster_dct["clash blaster neo"]["role"] = "slayer, support"
    blaster_dct["clash blaster neo"]["weight"] = "light"
    blaster_dct["clash blaster neo"]["impact"] = 30
    blaster_dct["clash blaster neo"]["fire rate"] = 65
    blaster_dct["clash blaster neo"]["special points"] = 170

    blaster_dct["custom blaster"]["sub"] = "point sensor"
    blaster_dct["custom blaster"]["special"] = "triple splashdown"
    blaster_dct["custom blaster"]["points"] = 0
    blaster_dct["custom blaster"]["range"] = 27
    blaster_dct["custom blaster"]["role"] = "slayer"
    blaster_dct["custom blaster"]["weight"] = "middle"
    blaster_dct["custom blaster"]["impact"] = 70
    blaster_dct["custom blaster"]["fire rate"] = 20
    blaster_dct["custom blaster"]["special points"] = 180

    blaster_dct["luna blaster"]["sub"] = "splat bomb"
    blaster_dct["luna blaster"]["special"] = "zipcaster"
    blaster_dct["luna blaster"]["points"] = 0
    blaster_dct["luna blaster"]["range"] = 18
    blaster_dct["luna blaster"]["role"] = "slayer, support"
    blaster_dct["luna blaster"]["weight"] = "light"
    blaster_dct["luna blaster"]["impact"] = 70
    blaster_dct["luna blaster"]["fire rate"] = 30
    blaster_dct["luna blaster"]["special points"] = 180

    blaster_dct["luna blaster neo"]["sub"] = "fizzy bomb"
    blaster_dct["luna blaster neo"]["special"] = "ultra stamp"
    blaster_dct["luna blaster neo"]["points"] = 0
    blaster_dct["luna blaster neo"]["range"] = 18
    blaster_dct["luna blaster neo"]["role"] = "slayer, support"
    blaster_dct["luna blaster neo"]["weight"] = "light"
    blaster_dct["luna blaster neo"]["impact"] = 70
    blaster_dct["luna blaster neo"]["fire rate"] = 30
    blaster_dct["luna blaster neo"]["special points"] = 180

    blaster_dct["range blaster"]["sub"] = "suction bomb"
    blaster_dct["range blaster"]["special"] = "wave breaker"
    blaster_dct["range blaster"]["points"] = 0
    blaster_dct["range blaster"]["range"] = 56
    blaster_dct["range blaster"]["role"] = "slayer, support"
    blaster_dct["range blaster"]["weight"] = "middle"
    blaster_dct["range blaster"]["impact"] = 70
    blaster_dct["range blaster"]["fire rate"] = 10
    blaster_dct["range blaster"]["special points"] = 200

    blaster_dct["rapid blaster"]["sub"] = "ink mine"
    blaster_dct["rapid blaster"]["special"] = "triple inkstrike"
    blaster_dct["rapid blaster"]["points"] = 0
    blaster_dct["rapid blaster"]["range"] = 62
    blaster_dct["rapid blaster"]["role"] = "slayer"
    blaster_dct["rapid blaster"]["weight"] = "middle"
    blaster_dct["rapid blaster"]["impact"] = 35
    blaster_dct["rapid blaster"]["fire rate"] = 40
    blaster_dct["rapid blaster"]["special points"] = 190

    blaster_dct["rapid blaster deco"]["sub"] = "torpedo"
    blaster_dct["rapid blaster deco"]["special"] = "inkjet"
    blaster_dct["rapid blaster deco"]["points"] = 0
    blaster_dct["rapid blaster deco"]["range"] = 62
    blaster_dct["rapid blaster deco"]["role"] = "slayer"
    blaster_dct["rapid blaster deco"]["weight"] = "middle"
    blaster_dct["rapid blaster deco"]["impact"] = 35
    blaster_dct["rapid blaster deco"]["fire rate"] = 40
    blaster_dct["rapid blaster deco"]["special points"] = 210

    blaster_dct["rapid blaster pro"]["sub"] = "toxic mist"
    blaster_dct["rapid blaster pro"]["special"] = "ink vac"
    blaster_dct["rapid blaster pro"]["points"] = 0
    blaster_dct["rapid blaster pro"]["range"] = 72
    blaster_dct["rapid blaster pro"]["role"] = "anchor, support"
    blaster_dct["rapid blaster pro"]["weight"] = "middle"
    blaster_dct["rapid blaster pro"]["impact"] = 35
    blaster_dct["rapid blaster pro"]["fire rate"] = 30
    blaster_dct["rapid blaster pro"]["special points"] = 180

    blaster_dct["rapid blaster pro deco"]["sub"] = "angle shooter"
    blaster_dct["rapid blaster pro deco"]["special"] = "killer wail 5.1"
    blaster_dct["rapid blaster pro deco"]["points"] = 0
    blaster_dct["rapid blaster pro deco"]["range"] = 72
    blaster_dct["rapid blaster pro deco"]["role"] = "anchor, support"
    blaster_dct["rapid blaster pro deco"]["weight"] = "middle"
    blaster_dct["rapid blaster pro deco"]["impact"] = 35
    blaster_dct["rapid blaster pro deco"]["fire rate"] = 30
    blaster_dct["rapid blaster pro deco"]["special points"] = 190

    blaster_dct["s-blast '91"]["sub"] = "burst bomb"
    blaster_dct["s-blast '91"]["special"] = "booyah bomb"
    blaster_dct["s-blast '91"]["points"] = 0
    blaster_dct["s-blast '91"]["range"] = 45
    blaster_dct["s-blast '91"]["role"] = "slayer"
    blaster_dct["s-blast '91"]["weight"] = "middle"
    blaster_dct["s-blast '91"]["impact"] = 70
    blaster_dct["s-blast '91"]["fire rate"] = 10
    blaster_dct["s-blast '91"]["special points"] = 190

    blaster_dct["s-blast '92"]["sub"] = "sprinkler"
    blaster_dct["s-blast '92"]["special"] = "reefslider"
    blaster_dct["s-blast '92"]["points"] = 0
    blaster_dct["s-blast '92"]["range"] = 45
    blaster_dct["s-blast '92"]["role"] = "slayer"
    blaster_dct["s-blast '92"]["weight"] = "middle"
    blaster_dct["s-blast '92"]["impact"] = 70
    blaster_dct["s-blast '92"]["fire rate"] = 10
    blaster_dct["s-blast '92"]["special points"] = 180

    return blaster_dct


def build_brellas() -> dict:
    """
    Creates the brella dictionary
    class specifics: damage, durability
    :return: the brella dictionary
    """
    brellas = ["sorella brella", "splat brella", "tenta brella",
               "tenta sorella brella", "undercover brella", "undercover sorella brella"]

    brellas_dct = dict()
    for brella in brellas:
        brellas_dct[brella] = dict()

    brellas_dct["spec A"] = ("damage", 1)
    brellas_dct["spec B"] = ("durability", 1)

    brellas_dct["sorella brella"]["sub"] = "autobomb"
    brellas_dct["sorella brella"]["special"] = "inkjet"
    brellas_dct["sorella brella"]["points"] = 0
    brellas_dct["sorella brella"]["range"] = 43
    brellas_dct["sorella brella"]["role"] = "skirmisher, support"
    brellas_dct["sorella brella"]["weight"] = "middle"
    brellas_dct["sorella brella"]["damage"] = 65
    brellas_dct["sorella brella"]["durability"] = 60
    brellas_dct["sorella brella"]["special points"] = 190

    brellas_dct["splat brella"]["sub"] = "sprinkler"
    brellas_dct["splat brella"]["special"] = "triple inkstrike"
    brellas_dct["splat brella"]["points"] = 0
    brellas_dct["splat brella"]["range"] = 43
    brellas_dct["splat brella"]["role"] = "support"
    brellas_dct["splat brella"]["weight"] = "middle"
    brellas_dct["splat brella"]["damage"] = 65
    brellas_dct["splat brella"]["durability"] = 60
    brellas_dct["splat brella"]["special points"] = 200

    brellas_dct["tenta brella"]["sub"] = "squid beakon"
    brellas_dct["tenta brella"]["special"] = "ink vac"
    brellas_dct["tenta brella"]["points"] = 0
    brellas_dct["tenta brella"]["range"] = 62
    brellas_dct["tenta brella"]["role"] = "skirmisher, slayer"
    brellas_dct["tenta brella"]["weight"] = "heavy"
    brellas_dct["tenta brella"]["damage"] = 85
    brellas_dct["tenta brella"]["durability"] = 85
    brellas_dct["tenta brella"]["special points"] = 190

    brellas_dct["tenta sorella brella"]["sub"] = "ink mine"
    brellas_dct["tenta sorella brella"]["special"] = "trizooka"
    brellas_dct["tenta sorella brella"]["points"] = 0
    brellas_dct["tenta sorella brella"]["range"] = 62
    brellas_dct["tenta sorella brella"]["role"] = "skirmisher, slayer"
    brellas_dct["tenta sorella brella"]["weight"] = "heavy"
    brellas_dct["tenta sorella brella"]["damage"] = 85
    brellas_dct["tenta sorella brella"]["durability"] = 85
    brellas_dct["tenta sorella brella"]["special points"] = 200

    brellas_dct["undercover brella"]["sub"] = "ink mine"
    brellas_dct["undercover brella"]["special"] = "reefslider"
    brellas_dct["undercover brella"]["points"] = 0
    brellas_dct["undercover brella"]["range"] = 50
    brellas_dct["undercover brella"]["role"] = "skirmisher"
    brellas_dct["undercover brella"]["weight"] = "light"
    brellas_dct["undercover brella"]["damage"] = 30
    brellas_dct["undercover brella"]["durability"] = 25
    brellas_dct["undercover brella"]["special points"] = 180

    brellas_dct["undercover sorella brella"]["sub"] = "torpedo"
    brellas_dct["undercover sorella brella"]["special"] = "splattercolor screen"
    brellas_dct["undercover sorella brella"]["points"] = 0
    brellas_dct["undercover sorella brella"]["range"] = 50
    brellas_dct["undercover sorella brella"]["role"] = "skirmisher"
    brellas_dct["undercover sorella brella"]["weight"] = "light"
    brellas_dct["undercover sorella brella"]["damage"] = 30
    brellas_dct["undercover sorella brella"]["durability"] = 25
    brellas_dct["undercover sorella brella"]["special points"] = 180

    return brellas_dct


def build_brushes() -> dict:
    """
    Creates the brush dictionary
    class specifics: ink speed, handling
    :return: the brush dictionary
    """
    brushes = ["inkbrush", "inkbrush nouveau", "octobrush", "octobrush nouveau", "painbrush", "painbrush nouveau"]

    brushes_dct = dict()
    for brush in brushes:
        brushes_dct[brush] = dict()

    brushes_dct["spec A"] = ("ink speed", 2)
    brushes_dct["spec B"] = ("handling", 2)

    brushes_dct["inkbrush"]["sub"] = "splat bomb"
    brushes_dct["inkbrush"]["special"] = "killer wail 5.1"
    brushes_dct["inkbrush"]["points"] = 0
    brushes_dct["inkbrush"]["range"] = 5
    brushes_dct["inkbrush"]["role"] = "skirmisher"
    brushes_dct["inkbrush"]["weight"] = "light"
    brushes_dct["inkbrush"]["ink speed"] = 100
    brushes_dct["inkbrush"]["handling"] = 100
    brushes_dct["inkbrush"]["special points"] = 180

    brushes_dct["inkbrush nouveau"]["sub"] = "ink mine"
    brushes_dct["inkbrush nouveau"]["special"] = "ultra stamp"
    brushes_dct["inkbrush nouveau"]["points"] = 0
    brushes_dct["inkbrush nouveau"]["range"] = 5
    brushes_dct["inkbrush nouveau"]["role"] = "skirmisher"
    brushes_dct["inkbrush nouveau"]["weight"] = "light"
    brushes_dct["inkbrush nouveau"]["ink speed"] = 100
    brushes_dct["inkbrush nouveau"]["handling"] = 100
    brushes_dct["inkbrush nouveau"]["special points"] = 180

    brushes_dct["octobrush"]["sub"] = "suction bomb"
    brushes_dct["octobrush"]["special"] = "zipcaster"
    brushes_dct["octobrush"]["points"] = 0
    brushes_dct["octobrush"]["range"] = 23
    brushes_dct["octobrush"]["role"] = "slayer, support"
    brushes_dct["octobrush"]["weight"] = "middle"
    brushes_dct["octobrush"]["ink speed"] = 80
    brushes_dct["octobrush"]["handling"] = 85
    brushes_dct["octobrush"]["special points"] = 200

    brushes_dct["octobrush nouveau"]["sub"] = "squid beakon"
    brushes_dct["octobrush nouveau"]["special"] = "ink storm"
    brushes_dct["octobrush nouveau"]["points"] = 0
    brushes_dct["octobrush nouveau"]["range"] = 23
    brushes_dct["octobrush nouveau"]["role"] = "slayer, support"
    brushes_dct["octobrush nouveau"]["weight"] = "middle"
    brushes_dct["octobrush nouveau"]["ink speed"] = 80
    brushes_dct["octobrush nouveau"]["handling"] = 85
    brushes_dct["octobrush nouveau"]["special points"] = 180

    brushes_dct["painbrush"]["sub"] = "curling bomb"
    brushes_dct["painbrush"]["special"] = "wave breaker"
    brushes_dct["painbrush"]["points"] = 0
    brushes_dct["painbrush"]["range"] = 33
    brushes_dct["painbrush"]["role"] = "anchor, slayer, support"
    brushes_dct["painbrush"]["weight"] = "middle"
    brushes_dct["painbrush"]["ink speed"] = 85
    brushes_dct["painbrush"]["handling"] = 60
    brushes_dct["painbrush"]["special points"] = 200

    brushes_dct["painbrush nouveau"]["sub"] = "point sensor"
    brushes_dct["painbrush nouveau"]["special"] = "tneta missiles"
    brushes_dct["painbrush nouveau"]["points"] = 0
    brushes_dct["painbrush nouveau"]["range"] = 33
    brushes_dct["painbrush nouveau"]["role"] = "anchor, slayer, support"
    brushes_dct["painbrush nouveau"]["weight"] = "middle"
    brushes_dct["painbrush nouveau"]["ink speed"] = 85
    brushes_dct["painbrush nouveau"]["handling"] = 60
    brushes_dct["painbrush nouveau"]["special points"] = 190

    return brushes_dct


def build_chargers() -> dict:
    """
    Creates the charger dictionary
    class specifics: charge speed, mobility
    :return: the charger dictionary
    """
    chargers = ["bamboozler 14 mk I", "classic squiffer", "custom goo tuber", "e-liter 4k", "e-liter 4k scope",
                "goo tuber", "snipewriter 5b", "snipewriter 5h", "splat charger", "splatterscope",
                "z+f splat charger", "z+f splatterscope"]

    chargers_dct = dict()
    for charger in chargers:
        chargers_dct[charger] = dict()

    chargers_dct["spec A"] = ("charge speed", 3)
    chargers_dct["spec B"] = ("mobility", 3)

    chargers_dct["bamboozler 14 mk I"]["sub"] = "autobomb"
    chargers_dct["bamboozler 14 mk I"]["special"] = "killer wail 5.1"
    chargers_dct["bamboozler 14 mk I"]["points"] = 0
    chargers_dct["bamboozler 14 mk I"]["range"] = 78
    chargers_dct["bamboozler 14 mk I"]["role"] = "anchor"
    chargers_dct["bamboozler 14 mk I"]["weight"] = "light"
    chargers_dct["bamboozler 14 mk I"]["charge speed"] = 90
    chargers_dct["bamboozler 14 mk I"]["mobility"] = 80
    chargers_dct["bamboozler 14 mk I"]["special points"] = 200

    chargers_dct["classic squiffer"]["sub"] = "point sensor"
    chargers_dct["classic squiffer"]["special"] = "big bubbler"
    chargers_dct["classic squiffer"]["points"] = 0
    chargers_dct["classic squiffer"]["range"] = 75
    chargers_dct["classic squiffer"]["role"] = "anchor, slayer"
    chargers_dct["classic squiffer"]["weight"] = "middle"
    chargers_dct["classic squiffer"]["charge speed"] = 70
    chargers_dct["classic squiffer"]["mobility"] = 60
    chargers_dct["classic squiffer"]["special points"] = 190

    chargers_dct["custom goo tuber"]["sub"] = "fizzy bomb"
    chargers_dct["custom goo tuber"]["special"] = "ultra stamp"
    chargers_dct["custom goo tuber"]["points"] = 0
    chargers_dct["custom goo tuber"]["range"] = 78
    chargers_dct["custom goo tuber"]["role"] = "slayer"
    chargers_dct["custom goo tuber"]["weight"] = "middle"
    chargers_dct["custom goo tuber"]["charge speed"] = 38
    chargers_dct["custom goo tuber"]["mobility"] = 70
    chargers_dct["custom goo tuber"]["special points"] = 200

    chargers_dct["e-liter 4k"]["sub"] = "ink mine"
    chargers_dct["e-liter 4k"]["special"] = "wave breaker"
    chargers_dct["e-liter 4k"]["points"] = 0
    chargers_dct["e-liter 4k"]["range"] = 96
    chargers_dct["e-liter 4k"]["role"] = "anchor"
    chargers_dct["e-liter 4k"]["weight"] = "heavy"
    chargers_dct["e-liter 4k"]["charge speed"] = 20
    chargers_dct["e-liter 4k"]["mobility"] = 15
    chargers_dct["e-liter 4k"]["special points"] = 210

    chargers_dct["e-liter 4k scope"]["sub"] = "ink mine"
    chargers_dct["e-liter 4k scope"]["special"] = "wave breaker"
    chargers_dct["e-liter 4k scope"]["points"] = 0
    chargers_dct["e-liter 4k scope"]["range"] = 100
    chargers_dct["e-liter 4k scope"]["role"] = "anchor"
    chargers_dct["e-liter 4k scope"]["weight"] = "heavy"
    chargers_dct["e-liter 4k scope"]["charge speed"] = 20
    chargers_dct["e-liter 4k scope"]["mobility"] = 5
    chargers_dct["e-liter 4k scope"]["special points"] = 210

    chargers_dct["goo tuber"]["sub"] = "torpedo"
    chargers_dct["goo tuber"]["special"] = "tenta missiles"
    chargers_dct["goo tuber"]["points"] = 0
    chargers_dct["goo tuber"]["range"] = 78
    chargers_dct["goo tuber"]["role"] = "slayer, support"
    chargers_dct["goo tuber"]["weight"] = "middle"
    chargers_dct["goo tuber"]["charge speed"] = 38
    chargers_dct["goo tuber"]["mobility"] = 70
    chargers_dct["goo tuber"]["special points"] = 200

    chargers_dct["snipewriter 5b"]["sub"] = "splash wall"
    chargers_dct["snipewriter 5b"]["special"] = "ink storm"
    chargers_dct["snipewriter 5b"]["points"] = 0
    chargers_dct["snipewriter 5b"]["range"] = 91
    chargers_dct["snipewriter 5b"]["role"] = "anchor, support"
    chargers_dct["snipewriter 5b"]["weight"] = "middle"
    chargers_dct["snipewriter 5b"]["charge speed"] = 43
    chargers_dct["snipewriter 5b"]["mobility"] = 80
    chargers_dct["snipewriter 5b"]["special points"] = 210

    chargers_dct["snipewriter 5h"]["sub"] = "sprinkler"
    chargers_dct["snipewriter 5h"]["special"] = "tacticooler"
    chargers_dct["snipewriter 5h"]["points"] = 0
    chargers_dct["snipewriter 5h"]["range"] = 91
    chargers_dct["snipewriter 5h"]["role"] = "anchor, support"
    chargers_dct["snipewriter 5h"]["weight"] = "middle"
    chargers_dct["snipewriter 5h"]["charge speed"] = 43
    chargers_dct["snipewriter 5h"]["mobility"] = 80
    chargers_dct["snipewriter 5h"]["special points"] = 200

    chargers_dct["splat charger"]["sub"] = "splat bomb"
    chargers_dct["splat charger"]["special"] = "ink vac"
    chargers_dct["splat charger"]["points"] = 0
    chargers_dct["splat charger"]["range"] = 88
    chargers_dct["splat charger"]["role"] = "anchor, support"
    chargers_dct["splat charger"]["weight"] = "middle"
    chargers_dct["splat charger"]["charge speed"] = 50
    chargers_dct["splat charger"]["mobility"] = 40
    chargers_dct["splat charger"]["special points"] = 200

    chargers_dct["splatterscope"]["sub"] = "splat bomb"
    chargers_dct["splatterscope"]["special"] = "ink vac"
    chargers_dct["splatterscope"]["points"] = 0
    chargers_dct["splatterscope"]["range"] = 91
    chargers_dct["splatterscope"]["role"] = "anchor"
    chargers_dct["splatterscope"]["weight"] = "middle"
    chargers_dct["splatterscope"]["charge speed"] = 50
    chargers_dct["splatterscope"]["mobility"] = 30
    chargers_dct["splatterscope"]["special points"] = 200

    chargers_dct["z+f splat charger"]["sub"] = "splash wall"
    chargers_dct["z+f splat charger"]["special"] = "triple inkstrike"
    chargers_dct["z+f splat charger"]["points"] = 0
    chargers_dct["z+f splat charger"]["range"] = 88
    chargers_dct["z+f splat charger"]["role"] = "slayer, support"
    chargers_dct["z+f splat charger"]["weight"] = "middle"
    chargers_dct["z+f splat charger"]["charge speed"] = 50
    chargers_dct["z+f splat charger"]["mobility"] = 40
    chargers_dct["z+f splat charger"]["special points"] = 210

    chargers_dct["z+f splatterscope"]["sub"] = "splash wall"
    chargers_dct["z+f splatterscope"]["special"] = "triple inkstrike"
    chargers_dct["z+f splatterscope"]["points"] = 0
    chargers_dct["z+f splatterscope"]["range"] = 91
    chargers_dct["z+f splatterscope"]["role"] = "slayer, support"
    chargers_dct["z+f splatterscope"]["weight"] = "middle"
    chargers_dct["z+f splatterscope"]["charge speed"] = 50
    chargers_dct["z+f splatterscope"]["mobility"] = 40
    chargers_dct["z+f splatterscope"]["special points"] = 210

    return chargers_dct


def build_dualies() -> dict:
    """
    Creates the dualies dictionary
    class specifics: damage, mobility
    :return: the dualies dictionary
    """
    dualies = ["custom dualie squelchers", "dapple dualies", "dapple dualies nouveau", "dark tetra dualies",
               "dualie squelchers", "enperry splat dualies", "glooga dualies", "light tetra dualies", "splat dualies"]

    dualies_dct = dict()
    for weapon in dualies:
        dualies_dct[weapon] = dict()

    dualies_dct["spec A"] = ("damage", 1)
    dualies_dct["spec B"] = ("mobility", 3)

    dualies_dct["custom dualie squelchers"]["sub"] = "squid beakon"
    dualies_dct["custom dualie squelchers"]["special"] = "super chump"
    dualies_dct["custom dualie squelchers"]["points"] = 0
    dualies_dct["custom dualie squelchers"]["range"] = 70
    dualies_dct["custom dualie squelchers"]["role"] = "skirmisher, slayer, support"
    dualies_dct["custom dualie squelchers"]["weight"] = "middle"
    dualies_dct["custom dualie squelchers"]["damage"] = 22
    dualies_dct["custom dualie squelchers"]["mobility"] = 70
    dualies_dct["custom dualie squelchers"]["special points"] = 210

    dualies_dct["dapple dualies"]["sub"] = "squid beakon"
    dualies_dct["dapple dualies"]["special"] = "tacticooler"
    dualies_dct["dapple dualies"]["points"] = 0
    dualies_dct["dapple dualies"]["range"] = 24
    dualies_dct["dapple dualies"]["role"] = "slayer, support"
    dualies_dct["dapple dualies"]["weight"] = "light"
    dualies_dct["dapple dualies"]["damage"] = 47
    dualies_dct["dapple dualies"]["mobility"] = 80
    dualies_dct["dapple dualies"]["special points"] = 180

    dualies_dct["dapple dualies nouveau"]["sub"] = "torpedo"
    dualies_dct["dapple dualies nouveau"]["special"] = "reefslider"
    dualies_dct["dapple dualies nouveau"]["points"] = 0
    dualies_dct["dapple dualies nouveau"]["range"] = 24
    dualies_dct["dapple dualies nouveau"]["role"] = "slayer"
    dualies_dct["dapple dualies nouveau"]["weight"] = "light"
    dualies_dct["dapple dualies nouveau"]["damage"] = 47
    dualies_dct["dapple dualies nouveau"]["mobility"] = 80
    dualies_dct["dapple dualies nouveau"]["special points"] = 190

    dualies_dct["dark tetra dualies"]["sub"] = "autobomb"
    dualies_dct["dark tetra dualies"]["special"] = "reefslider"
    dualies_dct["dark tetra dualies"]["points"] = 0
    dualies_dct["dark tetra dualies"]["range"] = 58
    dualies_dct["dark tetra dualies"]["role"] = "skirmisher, slayer"
    dualies_dct["dark tetra dualies"]["weight"] = "middle"
    dualies_dct["dark tetra dualies"]["damage"] = 22
    dualies_dct["dark tetra dualies"]["mobility"] = 90
    dualies_dct["dark tetra dualies"]["special points"] = 200

    dualies_dct["dualie squelchers"]["sub"] = "splat bomb"
    dualies_dct["dualie squelchers"]["special"] = "wave breaker"
    dualies_dct["dualie squelchers"]["points"] = 0
    dualies_dct["dualie squelchers"]["range"] = 70
    dualies_dct["dualie squelchers"]["role"] = "support"
    dualies_dct["dualie squelchers"]["weight"] = "middle"
    dualies_dct["dualie squelchers"]["damage"] = 22
    dualies_dct["dualie squelchers"]["mobility"] = 70
    dualies_dct["dualie squelchers"]["special points"] = 200

    dualies_dct["enperry splat dualies"]["sub"] = "curling bomb"
    dualies_dct["enperry splat dualies"]["special"] = "triple splashdown"
    dualies_dct["enperry splat dualies"]["points"] = 0
    dualies_dct["enperry splat dualies"]["range"] = 50
    dualies_dct["enperry splat dualies"]["role"] = "slayer, support"
    dualies_dct["enperry splat dualies"]["weight"] = "middle"
    dualies_dct["enperry splat dualies"]["damage"] = 29
    dualies_dct["enperry splat dualies"]["mobility"] = 60
    dualies_dct["enperry splat dualies"]["special points"] = 190

    dualies_dct["glooga dualies"]["sub"] = "splash wall"
    dualies_dct["glooga dualies"]["special"] = "booyah bomb"
    dualies_dct["glooga dualies"]["points"] = 0
    dualies_dct["glooga dualies"]["range"] = 66
    dualies_dct["glooga dualies"]["role"] = "slayer"
    dualies_dct["glooga dualies"]["weight"] = "middle"
    dualies_dct["glooga dualies"]["damage"] = 76
    dualies_dct["glooga dualies"]["mobility"] = 35
    dualies_dct["glooga dualies"]["special points"] = 180

    dualies_dct["light tetra dualies"]["sub"] = "sprinkler"
    dualies_dct["light tetra dualies"]["special"] = "zipcaster"
    dualies_dct["light tetra dualies"]["points"] = 0
    dualies_dct["light tetra dualies"]["range"] = 58
    dualies_dct["light tetra dualies"]["role"] = "skirmisher, slayer"
    dualies_dct["light tetra dualies"]["weight"] = "middle"
    dualies_dct["light tetra dualies"]["damage"] = 22
    dualies_dct["light tetra dualies"]["mobility"] = 90
    dualies_dct["light tetra dualies"]["special points"] = 190

    dualies_dct["splat dualies"]["sub"] = "suction bomb"
    dualies_dct["splat dualies"]["special"] = "crab tank"
    dualies_dct["splat dualies"]["points"] = 0
    dualies_dct["splat dualies"]["range"] = 50
    dualies_dct["splat dualies"]["role"] = "slayer, support"
    dualies_dct["splat dualies"]["weight"] = "middle"
    dualies_dct["splat dualies"]["damage"] = 29
    dualies_dct["splat dualies"]["mobility"] = 60
    dualies_dct["splat dualies"]["special points"] = 190

    return dualies_dct


def build_rollers() -> dict:
    """
    Creates the roller dictionary
    class specifics: ink speed, handling
    :return: the roller dictionary
    """
    rollers = ["big swig roller", "big swig roller express", "carbon roller", "carbon roller deco",
               "dynamo roller", "flingza roller", "gold dynamo roller", "krak-on splat roller", "splat roller"]

    rollers_dct = dict()
    for roller in rollers:
        rollers_dct[roller] = dict()

    rollers_dct["spec A"] = ("ink speed", 2)
    rollers_dct["spec B"] = ("handling", 2)

    rollers_dct["big swig roller"]["sub"] = "splash wall"
    rollers_dct["big swig roller"]["special"] = "ink vac"
    rollers_dct["big swig roller"]["points"] = 0
    rollers_dct["big swig roller"]["range"] = 56
    rollers_dct["big swig roller"]["role"] = "support"
    rollers_dct["big swig roller"]["weight"] = "middle"
    rollers_dct["big swig roller"]["ink speed"] = 54
    rollers_dct["big swig roller"]["handling"] = 60
    rollers_dct["big swig roller"]["special points"] = 190

    rollers_dct["big swig roller express"]["sub"] = "angle shooter"
    rollers_dct["big swig roller express"]["special"] = "ink storm"
    rollers_dct["big swig roller express"]["points"] = 0
    rollers_dct["big swig roller express"]["range"] = 56
    rollers_dct["big swig roller express"]["role"] = "support"
    rollers_dct["big swig roller express"]["weight"] = "middle"
    rollers_dct["big swig roller express"]["ink speed"] = 54
    rollers_dct["big swig roller express"]["handling"] = 60
    rollers_dct["big swig roller express"]["special points"] = 200

    rollers_dct["carbon roller"]["sub"] = "autobomb"
    rollers_dct["carbon roller"]["special"] = "zipcaster"
    rollers_dct["carbon roller"]["points"] = 0
    rollers_dct["carbon roller"]["range"] = 20
    rollers_dct["carbon roller"]["role"] = "slayer"
    rollers_dct["carbon roller"]["weight"] = "light"
    rollers_dct["carbon roller"]["ink speed"] = 63
    rollers_dct["carbon roller"]["handling"] = 65
    rollers_dct["carbon roller"]["special points"] = 170

    rollers_dct["carbon roller deco"]["sub"] = "burst bomb"
    rollers_dct["carbon roller deco"]["special"] = "trizooka"
    rollers_dct["carbon roller deco"]["points"] = 0
    rollers_dct["carbon roller deco"]["range"] = 20
    rollers_dct["carbon roller deco"]["role"] = "slayer"
    rollers_dct["carbon roller deco"]["weight"] = "light"
    rollers_dct["carbon roller deco"]["ink speed"] = 63
    rollers_dct["carbon roller deco"]["handling"] = 65
    rollers_dct["carbon roller deco"]["special points"] = 190

    rollers_dct["dynamo roller"]["sub"] = "sprinkler"
    rollers_dct["dynamo roller"]["special"] = "tacticooler"
    rollers_dct["dynamo roller"]["points"] = 0
    rollers_dct["dynamo roller"]["range"] = 76
    rollers_dct["dynamo roller"]["role"] = "anchor, support"
    rollers_dct["dynamo roller"]["weight"] = "heavy"
    rollers_dct["dynamo roller"]["ink speed"] = 25
    rollers_dct["dynamo roller"]["handling"] = 20
    rollers_dct["dynamo roller"]["special points"] = 190

    rollers_dct["flingza roller"]["sub"] = "ink mine"
    rollers_dct["flingza roller"]["special"] = "tenta missiles"
    rollers_dct["flingza roller"]["points"] = 0
    rollers_dct["flingza roller"]["range"] = 58
    rollers_dct["flingza roller"]["role"] = "support"
    rollers_dct["flingza roller"]["weight"] = "middle"
    rollers_dct["flingza roller"]["ink speed"] = 45
    rollers_dct["flingza roller"]["handling"] = 45
    rollers_dct["flingza roller"]["special points"] = 210

    rollers_dct["gold dynamo roller"]["sub"] = "splat bomb"
    rollers_dct["gold dynamo roller"]["special"] = "super chump"
    rollers_dct["gold dynamo roller"]["points"] = 0
    rollers_dct["gold dynamo roller"]["range"] = 76
    rollers_dct["gold dynamo roller"]["role"] = "anchor, support"
    rollers_dct["gold dynamo roller"]["weight"] = "heavy"
    rollers_dct["gold dynamo roller"]["ink speed"] = 25
    rollers_dct["gold dynamo roller"]["handling"] = 20
    rollers_dct["gold dynamo roller"]["special points"] = 190

    rollers_dct["krak-on splat roller"]["sub"] = "squid beakon"
    rollers_dct["krak-on splat roller"]["special"] = "kraken royale"
    rollers_dct["krak-on splat roller"]["points"] = 0
    rollers_dct["krak-on splat roller"]["range"] = 48
    rollers_dct["krak-on splat roller"]["role"] = "slayer, support"
    rollers_dct["krak-on splat roller"]["weight"] = "middle"
    rollers_dct["krak-on splat roller"]["ink speed"] = 45
    rollers_dct["krak-on splat roller"]["handling"] = 55
    rollers_dct["krak-on splat roller"]["special points"] = 180

    rollers_dct["splat roller"]["sub"] = "curling bomb"
    rollers_dct["splat roller"]["special"] = "big bubbler"
    rollers_dct["splat roller"]["points"] = 0
    rollers_dct["splat roller"]["range"] = 48
    rollers_dct["splat roller"]["role"] = "slayer, support"
    rollers_dct["splat roller"]["weight"] = "middle"
    rollers_dct["splat roller"]["ink speed"] = 45
    rollers_dct["splat roller"]["handling"] = 55
    rollers_dct["splat roller"]["special points"] = 180

    return rollers_dct


def build_shooters() -> dict:
    """
    Creates the shooter dictionary
    class specifics: damage, fire rate
    :return: the shooter dictionary
    """
    shooters = [".52 gal", ".96 gal", ".96 gal deco", "aerospray mg", "aerospray rg", "annaki splattershot nova",
                "custom jet squelcher", "custom splattershot jr", "foil squeezer", "forge splattershot pro",
                "h-3 nozzlenose", "h-3 nozzlenose d", "hero shot replica", "jet squelcher", "l-3 nozzlenose",
                "l-3 nozzlenose d", "n-zap '85", "n-zap '89", "neo splash-o-matic", "neo sploosh-o-matic",
                "splash-o-matic", "splattershot", "splattershot jr", "splattershot nova", "splattershot pro",
                "sploosh-o-matic", "squeezer", "tentatek splattershot"]

    shooters_dct = dict()
    for shooter in shooters:
        shooters_dct[shooter] = dict()

    shooters_dct["spec A"] = ("damage", 1)
    shooters_dct["spec B"] = ("fire rate", 0)

    shooters_dct[".52 gal"]["sub"] = "splash wall"
    shooters_dct[".52 gal"]["special"] = "killer wail 5.1"
    shooters_dct[".52 gal"]["points"] = 0
    shooters_dct[".52 gal"]["range"] = 55
    shooters_dct[".52 gal"]["role"] = "slayer"
    shooters_dct[".52 gal"]["weight"] = "middle"
    shooters_dct[".52 gal"]["damage"] = 75
    shooters_dct[".52 gal"]["fire rate"] = 25
    shooters_dct[".52 gal"]["special points"] = 190

    shooters_dct[".96 gal"]["sub"] = "sprinkler"
    shooters_dct[".96 gal"]["special"] = "ink vac"
    shooters_dct[".96 gal"]["points"] = 0
    shooters_dct[".96 gal"]["range"] = 74
    shooters_dct[".96 gal"]["role"] = "support"
    shooters_dct[".96 gal"]["weight"] = "middle"
    shooters_dct[".96 gal"]["damage"] = 80
    shooters_dct[".96 gal"]["fire rate"] = 10
    shooters_dct[".96 gal"]["special points"] = 190

    shooters_dct[".96 gal deco"]["sub"] = "splash wall"
    shooters_dct[".96 gal deco"]["special"] = "kraken royale"
    shooters_dct[".96 gal deco"]["points"] = 0
    shooters_dct[".96 gal deco"]["range"] = 74
    shooters_dct[".96 gal deco"]["role"] = "skirmisher"
    shooters_dct[".96 gal deco"]["weight"] = "middle"
    shooters_dct[".96 gal deco"]["damage"] = 80
    shooters_dct[".96 gal deco"]["fire rate"] = 10
    shooters_dct[".96 gal deco"]["special points"] = 210

    shooters_dct["aerospray mg"]["sub"] = "fizzy bomb"
    shooters_dct["aerospray mg"]["special"] = "reefslider"
    shooters_dct["aerospray mg"]["points"] = 0
    shooters_dct["aerospray mg"]["range"] = 35
    shooters_dct["aerospray mg"]["role"] = "support"
    shooters_dct["aerospray mg"]["weight"] = "light"
    shooters_dct["aerospray mg"]["damage"] = 10
    shooters_dct["aerospray mg"]["fire rate"] = 90
    shooters_dct["aerospray mg"]["special points"] = 180

    shooters_dct["aerospray rg"]["sub"] = "sprinkler"
    shooters_dct["aerospray rg"]["special"] = "booyah bomb"
    shooters_dct["aerospray rg"]["points"] = 0
    shooters_dct["aerospray rg"]["range"] = 35
    shooters_dct["aerospray rg"]["role"] = "support"
    shooters_dct["aerospray rg"]["weight"] = "light"
    shooters_dct["aerospray rg"]["damage"] = 10
    shooters_dct["aerospray rg"]["fire rate"] = 90
    shooters_dct["aerospray rg"]["special points"] = 210

    shooters_dct["annaki splattershot nova"]["sub"] = "ink mine"
    shooters_dct["annaki splattershot nova"]["special"] = "inkjet"
    shooters_dct["annaki splattershot nova"]["points"] = 0
    shooters_dct["annaki splattershot nova"]["range"] = 68
    shooters_dct["annaki splattershot nova"]["role"] = "support"
    shooters_dct["annaki splattershot nova"]["weight"] = "middle"
    shooters_dct["annaki splattershot nova"]["damage"] = 10
    shooters_dct["annaki splattershot nova"]["fire rate"] = 60
    shooters_dct["annaki splattershot nova"]["special points"] = 210

    shooters_dct["custom jet squelcher"]["sub"] = "toxic mist"
    shooters_dct["custom jet squelcher"]["special"] = "ink storm"
    shooters_dct["custom jet squelcher"]["points"] = 0
    shooters_dct["custom jet squelcher"]["range"] = 82
    shooters_dct["custom jet squelcher"]["role"] = "anchor, support"
    shooters_dct["custom jet squelcher"]["weight"] = "middle"
    shooters_dct["custom jet squelcher"]["damage"] = 35
    shooters_dct["custom jet squelcher"]["fire rate"] = 30
    shooters_dct["custom jet squelcher"]["special points"] = 180

    shooters_dct["custom splattershot jr"]["sub"] = "torpedo"
    shooters_dct["custom splattershot jr"]["special"] = "wave breaker"
    shooters_dct["custom splattershot jr"]["points"] = 0
    shooters_dct["custom splattershot jr"]["range"] = 35
    shooters_dct["custom splattershot jr"]["role"] = "support"
    shooters_dct["custom splattershot jr"]["weight"] = "light"
    shooters_dct["custom splattershot jr"]["damage"] = 22
    shooters_dct["custom splattershot jr"]["fire rate"] = 75
    shooters_dct["custom splattershot jr"]["special points"] = 190

    shooters_dct["foil squeezer"]["sub"] = "autobomb"
    shooters_dct["foil squeezer"]["special"] = "splattercolor screen"
    shooters_dct["foil squeezer"]["points"] = 0
    shooters_dct["foil squeezer"]["range"] = 77
    shooters_dct["foil squeezer"]["role"] = "skirmisher, slayer"
    shooters_dct["foil squeezer"]["weight"] = "middle"
    shooters_dct["foil squeezer"]["damage"] = 52
    shooters_dct["foil squeezer"]["fire rate"] = 30
    shooters_dct["foil squeezer"]["special points"] = 190

    shooters_dct["forge splattershot pro"]["sub"] = "suction bomb"
    shooters_dct["forge splattershot pro"]["special"] = "booyah bomb"
    shooters_dct["forge splattershot pro"]["points"] = 0
    shooters_dct["forge splattershot pro"]["range"] = 70
    shooters_dct["forge splattershot pro"]["role"] = "slayer"
    shooters_dct["forge splattershot pro"]["weight"] = "middle"
    shooters_dct["forge splattershot pro"]["damage"] = 60
    shooters_dct["forge splattershot pro"]["fire rate"] = 30
    shooters_dct["forge splattershot pro"]["special points"] = 210

    shooters_dct["h-3 nozzlenose"]["sub"] = "point sensor"
    shooters_dct["h-3 nozzlenose"]["special"] = "tacticooler"
    shooters_dct["h-3 nozzlenose"]["points"] = 0
    shooters_dct["h-3 nozzlenose"]["range"] = 70
    shooters_dct["h-3 nozzlenose"]["role"] = "slayer, support"
    shooters_dct["h-3 nozzlenose"]["weight"] = "middle"
    shooters_dct["h-3 nozzlenose"]["damage"] = 58
    shooters_dct["h-3 nozzlenose"]["fire rate"] = 30
    shooters_dct["h-3 nozzlenose"]["special points"] = 190

    shooters_dct["h-3 nozzlenose d"]["sub"] = "splash wall"
    shooters_dct["h-3 nozzlenose d"]["special"] = "big bubbler"
    shooters_dct["h-3 nozzlenose d"]["points"] = 0
    shooters_dct["h-3 nozzlenose d"]["range"] = 70
    shooters_dct["h-3 nozzlenose d"]["role"] = "slayer, support"
    shooters_dct["h-3 nozzlenose d"]["weight"] = "middle"
    shooters_dct["h-3 nozzlenose d"]["damage"] = 58
    shooters_dct["h-3 nozzlenose d"]["fire rate"] = 30
    shooters_dct["h-3 nozzlenose d"]["special points"] = 200

    shooters_dct["hero shot replica"]["sub"] = "suction bomb"
    shooters_dct["hero shot replica"]["special"] = "trizooka"
    shooters_dct["hero shot replica"]["points"] = 0
    shooters_dct["hero shot replica"]["range"] = 50
    shooters_dct["hero shot replica"]["role"] = "slayer"
    shooters_dct["hero shot replica"]["weight"] = "middle"
    shooters_dct["hero shot replica"]["damage"] = 47
    shooters_dct["hero shot replica"]["fire rate"] = 60
    shooters_dct["hero shot replica"]["special points"] = 190

    shooters_dct["jet squelcher"]["sub"] = "angle shooter"
    shooters_dct["jet squelcher"]["special"] = "ink vac"
    shooters_dct["jet squelcher"]["points"] = 0
    shooters_dct["jet squelcher"]["range"] = 82
    shooters_dct["jet squelcher"]["role"] = "anchor, support"
    shooters_dct["jet squelcher"]["weight"] = "middle"
    shooters_dct["jet squelcher"]["damage"] = 35
    shooters_dct["jet squelcher"]["fire rate"] = 30
    shooters_dct["jet squelcher"]["special points"] = 180

    shooters_dct["l-3 nozzlenose"]["sub"] = "curling bomb"
    shooters_dct["l-3 nozzlenose"]["special"] = "crab tank"
    shooters_dct["l-3 nozzlenose"]["points"] = 0
    shooters_dct["l-3 nozzlenose"]["range"] = 62
    shooters_dct["l-3 nozzlenose"]["role"] = "slayer"
    shooters_dct["l-3 nozzlenose"]["weight"] = "middle"
    shooters_dct["l-3 nozzlenose"]["damage"] = 25
    shooters_dct["l-3 nozzlenose"]["fire rate"] = 65
    shooters_dct["l-3 nozzlenose"]["special points"] = 190

    shooters_dct["l-3 nozzlenose d"]["sub"] = "burst bomb"
    shooters_dct["l-3 nozzlenose d"]["special"] = "ultra stamp"
    shooters_dct["l-3 nozzlenose d"]["points"] = 0
    shooters_dct["l-3 nozzlenose d"]["range"] = 62
    shooters_dct["l-3 nozzlenose d"]["role"] = "slayer"
    shooters_dct["l-3 nozzlenose d"]["weight"] = "middle"
    shooters_dct["l-3 nozzlenose d"]["damage"] = 25
    shooters_dct["l-3 nozzlenose d"]["fire rate"] = 65
    shooters_dct["l-3 nozzlenose d"]["special points"] = 200

    shooters_dct["n-zap '85"]["sub"] = "suction bomb"
    shooters_dct["n-zap '85"]["special"] = "tacticooler"
    shooters_dct["n-zap '85"]["points"] = 0
    shooters_dct["n-zap '85"]["range"] = 50
    shooters_dct["n-zap '85"]["role"] = "slayer, support"
    shooters_dct["n-zap '85"]["weight"] = "light"
    shooters_dct["n-zap '85"]["damage"] = 22
    shooters_dct["n-zap '85"]["fire rate"] = 75
    shooters_dct["n-zap '85"]["special points"] = 190

    shooters_dct["n-zap '89"]["sub"] = "autobomb"
    shooters_dct["n-zap '89"]["special"] = "super chump"
    shooters_dct["n-zap '89"]["points"] = 0
    shooters_dct["n-zap '89"]["range"] = 50
    shooters_dct["n-zap '89"]["role"] = "slayer, support"
    shooters_dct["n-zap '89"]["weight"] = "light"
    shooters_dct["n-zap '89"]["damage"] = 22
    shooters_dct["n-zap '89"]["fire rate"] = 75
    shooters_dct["n-zap '89"]["special points"] = 180

    shooters_dct["neo splash-o-matic"]["sub"] = "suction bomb"
    shooters_dct["neo splash-o-matic"]["special"] = "triple inkstrike"
    shooters_dct["neo splash-o-matic"]["points"] = 0
    shooters_dct["neo splash-o-matic"]["range"] = 42
    shooters_dct["neo splash-o-matic"]["role"] = "slayer, support"
    shooters_dct["neo splash-o-matic"]["weight"] = "light"
    shooters_dct["neo splash-o-matic"]["damage"] = 22
    shooters_dct["neo splash-o-matic"]["fire rate"] = 75
    shooters_dct["neo splash-o-matic"]["special points"] = 210

    shooters_dct["neo sploosh-o-matic"]["sub"] = "squid beakon"
    shooters_dct["neo sploosh-o-matic"]["special"] = "killer wail 5.1"
    shooters_dct["neo sploosh-o-matic"]["points"] = 0
    shooters_dct["neo sploosh-o-matic"]["range"] = 12
    shooters_dct["neo sploosh-o-matic"]["role"] = "slayer, support"
    shooters_dct["neo sploosh-o-matic"]["weight"] = "light"
    shooters_dct["neo sploosh-o-matic"]["damage"] = 52
    shooters_dct["neo sploosh-o-matic"]["fire rate"] = 75
    shooters_dct["neo sploosh-o-matic"]["special points"] = 180

    shooters_dct["splash-o-matic"]["sub"] = "burst bomb"
    shooters_dct["splash-o-matic"]["special"] = "crab tank"
    shooters_dct["splash-o-matic"]["points"] = 0
    shooters_dct["splash-o-matic"]["range"] = 42
    shooters_dct["splash-o-matic"]["role"] = "slayer, support"
    shooters_dct["splash-o-matic"]["weight"] = "light"
    shooters_dct["splash-o-matic"]["damage"] = 22
    shooters_dct["splash-o-matic"]["fire rate"] = 75
    shooters_dct["splash-o-matic"]["special points"] = 200

    shooters_dct["splattershot"]["sub"] = "suction bomb"
    shooters_dct["splattershot"]["special"] = "trizooka"
    shooters_dct["splattershot"]["points"] = 0
    shooters_dct["splattershot"]["range"] = 50
    shooters_dct["splattershot"]["role"] = "slayer"
    shooters_dct["splattershot"]["weight"] = "middle"
    shooters_dct["splattershot"]["damage"] = 47
    shooters_dct["splattershot"]["fire rate"] = 60
    shooters_dct["splattershot"]["special points"] = 190

    shooters_dct["splattershot jr"]["sub"] = "splat bomb"
    shooters_dct["splattershot jr"]["special"] = "big bubbler"
    shooters_dct["splattershot jr"]["points"] = 0
    shooters_dct["splattershot jr"]["range"] = 35
    shooters_dct["splattershot jr"]["role"] = "support"
    shooters_dct["splattershot jr"]["weight"] = "light"
    shooters_dct["splattershot jr"]["damage"] = 22
    shooters_dct["splattershot jr"]["fire rate"] = 75
    shooters_dct["splattershot jr"]["special points"] = 180

    shooters_dct["splattershot nova"]["sub"] = "point sensor"
    shooters_dct["splattershot nova"]["special"] = "killer wail 5.1"
    shooters_dct["splattershot nova"]["points"] = 0
    shooters_dct["splattershot nova"]["range"] = 68
    shooters_dct["splattershot nova"]["role"] = "support"
    shooters_dct["splattershot nova"]["weight"] = "middle"
    shooters_dct["splattershot nova"]["damage"] = 10
    shooters_dct["splattershot nova"]["fire rate"] = 60
    shooters_dct["splattershot nova"]["special points"] = 190

    shooters_dct["splattershot pro"]["sub"] = "angle shooter"
    shooters_dct["splattershot pro"]["special"] = "crab tank"
    shooters_dct["splattershot pro"]["points"] = 0
    shooters_dct["splattershot pro"]["range"] = 70
    shooters_dct["splattershot pro"]["role"] = "slayer"
    shooters_dct["splattershot pro"]["weight"] = "middle"
    shooters_dct["splattershot pro"]["damage"] = 60
    shooters_dct["splattershot pro"]["fire rate"] = 30
    shooters_dct["splattershot pro"]["special points"] = 180

    shooters_dct["sploosh-o-matic"]["sub"] = "curling bomb"
    shooters_dct["sploosh-o-matic"]["special"] = "ultra stamp"
    shooters_dct["sploosh-o-matic"]["points"] = 0
    shooters_dct["sploosh-o-matic"]["range"] = 12
    shooters_dct["sploosh-o-matic"]["role"] = "slayer"
    shooters_dct["sploosh-o-matic"]["weight"] = "light"
    shooters_dct["sploosh-o-matic"]["damage"] = 52
    shooters_dct["sploosh-o-matic"]["fire rate"] = 75
    shooters_dct["sploosh-o-matic"]["special points"] = 180

    shooters_dct["squeezer"]["sub"] = "splash wall"
    shooters_dct["squeezer"]["special"] = "trizooka"
    shooters_dct["squeezer"]["points"] = 0
    shooters_dct["squeezer"]["range"] = 77
    shooters_dct["squeezer"]["role"] = "skirmisher, slayer"
    shooters_dct["squeezer"]["weight"] = "middle"
    shooters_dct["squeezer"]["damage"] = 52
    shooters_dct["squeezer"]["fire rate"] = 30
    shooters_dct["squeezer"]["special points"] = 210

    shooters_dct["tentatek splattershot"]["sub"] = "splat bomb"
    shooters_dct["tentatek splattershot"]["special"] = "triple inkstrike"
    shooters_dct["tentatek splattershot"]["points"] = 0
    shooters_dct["tentatek splattershot"]["range"] = 50
    shooters_dct["tentatek splattershot"]["role"] = "slayer"
    shooters_dct["tentatek splattershot"]["weight"] = "middle"
    shooters_dct["tentatek splattershot"]["damage"] = 47
    shooters_dct["tentatek splattershot"]["fire rate"] = 60
    shooters_dct["tentatek splattershot"]["special points"] = 190

    return shooters_dct


def build_sloshers() -> dict:
    """
    Creates the slosher dictionary
    class specifics: damage, handling
    :return: the slosher dictionary
    """
    sloshers = ["bloblobber", "bloblobber deco", "dread wringer", "explosher", "slosher", "slosher deco",
                "sloshing machine", "sloshing machine neo", "tri-slosher", "tri-slosher nouveau"]

    sloshers_dct = dict()
    for slosher in sloshers:
        sloshers_dct[slosher] = dict()

    sloshers_dct["spec A"] = ("damage", 1)
    sloshers_dct["spec B"] = ("handling", 2)

    sloshers_dct["bloblobber"]["sub"] = "sprinkler"
    sloshers_dct["bloblobber"]["special"] = "ink storm"
    sloshers_dct["bloblobber"]["points"] = 0
    sloshers_dct["bloblobber"]["range"] = 85
    sloshers_dct["bloblobber"]["role"] = "anchor, support"
    sloshers_dct["bloblobber"]["weight"] = "middle"
    sloshers_dct["bloblobber"]["damage"] = 29
    sloshers_dct["bloblobber"]["handling"] = 50
    sloshers_dct["bloblobber"]["special points"] = 190

    sloshers_dct["bloblobber deco"]["sub"] = "angle shooter"
    sloshers_dct["bloblobber deco"]["special"] = "kraken royale"
    sloshers_dct["bloblobber deco"]["points"] = 0
    sloshers_dct["bloblobber deco"]["range"] = 85
    sloshers_dct["bloblobber deco"]["role"] = "anchor, support"
    sloshers_dct["bloblobber deco"]["weight"] = "middle"
    sloshers_dct["bloblobber deco"]["damage"] = 29
    sloshers_dct["bloblobber deco"]["handling"] = 50
    sloshers_dct["bloblobber deco"]["special points"] = 200

    sloshers_dct["dread wringer"]["sub"] = "suction bomb"
    sloshers_dct["dread wringer"]["special"] = "reefslider"
    sloshers_dct["dread wringer"]["points"] = 0
    sloshers_dct["dread wringer"]["range"] = 60
    sloshers_dct["dread wringer"]["role"] = "skirmisher, support"
    sloshers_dct["dread wringer"]["weight"] = "middle"
    sloshers_dct["dread wringer"]["damage"] = 55
    sloshers_dct["dread wringer"]["handling"] = 35
    sloshers_dct["dread wringer"]["special points"] = 190

    sloshers_dct["explosher"]["sub"] = "point sensor"
    sloshers_dct["explosher"]["special"] = "ink storm"
    sloshers_dct["explosher"]["points"] = 0
    sloshers_dct["explosher"]["range"] = 77
    sloshers_dct["explosher"]["role"] = "anchor, skirmisher"
    sloshers_dct["explosher"]["weight"] = "heavy"
    sloshers_dct["explosher"]["damage"] = 65
    sloshers_dct["explosher"]["handling"] = 20
    sloshers_dct["explosher"]["special points"] = 200

    sloshers_dct["slosher"]["sub"] = "splat bomb"
    sloshers_dct["slosher"]["special"] = "triple inkstrike"
    sloshers_dct["slosher"]["points"] = 0
    sloshers_dct["slosher"]["range"] = 58
    sloshers_dct["slosher"]["role"] = "slayer, support"
    sloshers_dct["slosher"]["weight"] = "middle"
    sloshers_dct["slosher"]["damage"] = 85
    sloshers_dct["slosher"]["handling"] = 50
    sloshers_dct["slosher"]["special points"] = 200

    sloshers_dct["slosher deco"]["sub"] = "angle shooter"
    sloshers_dct["slosher deco"]["special"] = "zipcaster"
    sloshers_dct["slosher deco"]["points"] = 0
    sloshers_dct["slosher deco"]["range"] = 58
    sloshers_dct["slosher deco"]["role"] = "slayer"
    sloshers_dct["slosher deco"]["weight"] = "middle"
    sloshers_dct["slosher deco"]["damage"] = 85
    sloshers_dct["slosher deco"]["handling"] = 50
    sloshers_dct["slosher deco"]["special points"] = 180

    sloshers_dct["sloshing machine"]["sub"] = "fizzy bomb"
    sloshers_dct["sloshing machine"]["special"] = "booyah bomb"
    sloshers_dct["sloshing machine"]["points"] = 0
    sloshers_dct["sloshing machine"]["range"] = 60
    sloshers_dct["sloshing machine"]["role"] = "skirmisher, slayer"
    sloshers_dct["sloshing machine"]["weight"] = "middle"
    sloshers_dct["sloshing machine"]["damage"] = 90
    sloshers_dct["sloshing machine"]["handling"] = 40
    sloshers_dct["sloshing machine"]["special points"] = 220

    sloshers_dct["sloshing machine neo"]["sub"] = "point sensor"
    sloshers_dct["sloshing machine neo"]["special"] = "trizooka"
    sloshers_dct["sloshing machine neo"]["points"] = 0
    sloshers_dct["sloshing machine neo"]["range"] = 60
    sloshers_dct["sloshing machine neo"]["role"] = "skirmisher, slayer"
    sloshers_dct["sloshing machine neo"]["weight"] = "middle"
    sloshers_dct["sloshing machine neo"]["damage"] = 90
    sloshers_dct["sloshing machine neo"]["handling"] = 40
    sloshers_dct["sloshing machine neo"]["special points"] = 190

    sloshers_dct["tri-slosher"]["sub"] = "toxic mist"
    sloshers_dct["tri-slosher"]["special"] = "inkjet"
    sloshers_dct["tri-slosher"]["points"] = 0
    sloshers_dct["tri-slosher"]["range"] = 31
    sloshers_dct["tri-slosher"]["role"] = "slayer"
    sloshers_dct["tri-slosher"]["weight"] = "light"
    sloshers_dct["tri-slosher"]["damage"] = 75
    sloshers_dct["tri-slosher"]["handling"] = 70
    sloshers_dct["tri-slosher"]["special points"] = 180

    sloshers_dct["tri-slosher nouveau"]["sub"] = "fizzy bomb"
    sloshers_dct["tri-slosher nouveau"]["special"] = "tacticooler"
    sloshers_dct["tri-slosher nouveau"]["points"] = 0
    sloshers_dct["tri-slosher nouveau"]["range"] = 31
    sloshers_dct["tri-slosher nouveau"]["role"] = "slayer, support"
    sloshers_dct["tri-slosher nouveau"]["weight"] = "light"
    sloshers_dct["tri-slosher nouveau"]["damage"] = 75
    sloshers_dct["tri-slosher nouveau"]["handling"] = 70
    sloshers_dct["tri-slosher nouveau"]["special points"] = 200

    return sloshers_dct


def build_splatanas() -> dict:
    """
    Creates the splatana dictionary
    class specifics: damage, handling
    :return: the splatana dictionary
    """
    splatanas = ["neo splatana stamper", "splatana stamper", "splatana wiper", "splatana wiper deco"]

    splatanas_dct = dict()
    for splatana in splatanas:
        splatanas_dct[splatana] = dict()

    splatanas_dct["spec A"] = ("damage", 1)
    splatanas_dct["spec B"] = ("handling", 2)

    splatanas_dct["neo splatana stamper"]["sub"] = "toxic mist"
    splatanas_dct["neo splatana stamper"]["special"] = "crab tank"
    splatanas_dct["neo splatana stamper"]["points"] = 0
    splatanas_dct["neo splatana stamper"]["range"] = 75
    splatanas_dct["neo splatana stamper"]["role"] = "slayer"
    splatanas_dct["neo splatana stamper"]["weight"] = "middle"
    splatanas_dct["neo splatana stamper"]["damage"] = 43
    splatanas_dct["neo splatana stamper"]["handling"] = 60
    splatanas_dct["neo splatana stamper"]["special points"] = 210

    splatanas_dct["splatana stamper"]["sub"] = "burst bomb"
    splatanas_dct["splatana stamper"]["special"] = "zipcaster"
    splatanas_dct["splatana stamper"]["points"] = 0
    splatanas_dct["splatana stamper"]["range"] = 75
    splatanas_dct["splatana stamper"]["role"] = "slayer"
    splatanas_dct["splatana stamper"]["weight"] = "middle"
    splatanas_dct["splatana stamper"]["damage"] = 43
    splatanas_dct["splatana stamper"]["handling"] = 60
    splatanas_dct["splatana stamper"]["special points"] = 210

    splatanas_dct["splatana wiper"]["sub"] = "torpedo"
    splatanas_dct["splatana wiper"]["special"] = "ultra stamp"
    splatanas_dct["splatana wiper"]["points"] = 0
    splatanas_dct["splatana wiper"]["range"] = 58
    splatanas_dct["splatana wiper"]["role"] = "skirmisher"
    splatanas_dct["splatana wiper"]["weight"] = "light"
    splatanas_dct["splatana wiper"]["damage"] = 29
    splatanas_dct["splatana wiper"]["handling"] = 75
    splatanas_dct["splatana wiper"]["special points"] = 190

    splatanas_dct["splatana wiper deco"]["sub"] = "squid beakon"
    splatanas_dct["splatana wiper deco"]["special"] = "tenta missiles"
    splatanas_dct["splatana wiper deco"]["points"] = 0
    splatanas_dct["splatana wiper deco"]["range"] = 58
    splatanas_dct["splatana wiper deco"]["role"] = "skirmisher"
    splatanas_dct["splatana wiper deco"]["weight"] = "light"
    splatanas_dct["splatana wiper deco"]["damage"] = 29
    splatanas_dct["splatana wiper deco"]["handling"] = 75
    splatanas_dct["splatana wiper deco"]["special points"] = 190

    return splatanas_dct


def build_splatlings() -> dict:
    """
    Creates the splatling dictionary
    class specifics: charge speed, mobility
    :return: the splatling dictionary
    """
    splatlings = ["ballpoint splatling", "ballpoint splatling nouveau", "heavy edit splatling", "heavy splatling",
                  "heavy splatling deco", "hydra splatling", "mini splatling", "nautilus 47", "zink mini splatling"]

    splatlings_dct = dict()
    for splatling in splatlings:
        splatlings_dct[splatling] = dict()

    splatlings_dct["spec A"] = ("charge speed", 3)
    splatlings_dct["spec B"] = ("mobility", 3)

    splatlings_dct["ballpoint splatling"]["sub"] = "fizzy bomb"
    splatlings_dct["ballpoint splatling"]["special"] = "inkjet"
    splatlings_dct["ballpoint splatling"]["points"] = 0
    splatlings_dct["ballpoint splatling"]["range"] = 84
    splatlings_dct["ballpoint splatling"]["role"] = "anchor, slayer"
    splatlings_dct["ballpoint splatling"]["weight"] = "middle"
    splatlings_dct["ballpoint splatling"]["charge speed"] = 18
    splatlings_dct["ballpoint splatling"]["mobility"] = 60
    splatlings_dct["ballpoint splatling"]["special points"] = 210

    splatlings_dct["ballpoint splatling nouveau"]["sub"] = "ink mine"
    splatlings_dct["ballpoint splatling nouveau"]["special"] = "ink vac"
    splatlings_dct["ballpoint splatling nouveau"]["points"] = 0
    splatlings_dct["ballpoint splatling nouveau"]["range"] = 84
    splatlings_dct["ballpoint splatling nouveau"]["role"] = "anchor, support"
    splatlings_dct["ballpoint splatling nouveau"]["weight"] = "middle"
    splatlings_dct["ballpoint splatling nouveau"]["charge speed"] = 18
    splatlings_dct["ballpoint splatling nouveau"]["mobility"] = 60
    splatlings_dct["ballpoint splatling nouveau"]["special points"] = 200

    splatlings_dct["heavy edit splatling"]["sub"] = "curling bomb"
    splatlings_dct["heavy edit splatling"]["special"] = "tacticooler"
    splatlings_dct["heavy edit splatling"]["points"] = 0
    splatlings_dct["heavy edit splatling"]["range"] = 70
    splatlings_dct["heavy edit splatling"]["role"] = "anchor, support"
    splatlings_dct["heavy edit splatling"]["weight"] = "middle"
    splatlings_dct["heavy edit splatling"]["charge speed"] = 14
    splatlings_dct["heavy edit splatling"]["mobility"] = 90
    splatlings_dct["heavy edit splatling"]["special points"] = 190

    splatlings_dct["heavy splatling"]["sub"] = "sprinkler"
    splatlings_dct["heavy splatling"]["special"] = "wave breaker"
    splatlings_dct["heavy splatling"]["points"] = 0
    splatlings_dct["heavy splatling"]["range"] = 78
    splatlings_dct["heavy splatling"]["role"] = "anchor"
    splatlings_dct["heavy splatling"]["weight"] = "middle"
    splatlings_dct["heavy splatling"]["charge speed"] = 38
    splatlings_dct["heavy splatling"]["mobility"] = 55
    splatlings_dct["heavy splatling"]["special points"] = 200

    splatlings_dct["heavy splatling deco"]["sub"] = "point sensor"
    splatlings_dct["heavy splatling deco"]["special"] = "kraken royale"
    splatlings_dct["heavy splatling deco"]["points"] = 0
    splatlings_dct["heavy splatling deco"]["range"] = 78
    splatlings_dct["heavy splatling deco"]["role"] = "anchor"
    splatlings_dct["heavy splatling deco"]["weight"] = "middle"
    splatlings_dct["heavy splatling deco"]["charge speed"] = 38
    splatlings_dct["heavy splatling deco"]["mobility"] = 55
    splatlings_dct["heavy splatling deco"]["special points"] = 200

    splatlings_dct["hydra splatling"]["sub"] = "autobomb"
    splatlings_dct["hydra splatling"]["special"] = "booyah bomb"
    splatlings_dct["hydra splatling"]["points"] = 0
    splatlings_dct["hydra splatling"]["range"] = 85
    splatlings_dct["hydra splatling"]["role"] = "anchor"
    splatlings_dct["hydra splatling"]["weight"] = "heavy"
    splatlings_dct["hydra splatling"]["charge speed"] = 10
    splatlings_dct["hydra splatling"]["mobility"] = 20
    splatlings_dct["hydra splatling"]["special points"] = 190

    splatlings_dct["mini splatling"]["sub"] = "burst bomb"
    splatlings_dct["mini splatling"]["special"] = "ultra stamp"
    splatlings_dct["mini splatling"]["points"] = 0
    splatlings_dct["mini splatling"]["range"] = 62
    splatlings_dct["mini splatling"]["role"] = "support"
    splatlings_dct["mini splatling"]["weight"] = "middle"
    splatlings_dct["mini splatling"]["charge speed"] = 80
    splatlings_dct["mini splatling"]["mobility"] = 90
    splatlings_dct["mini splatling"]["special points"] = 190

    splatlings_dct["nautilus 47"]["sub"] = "point sensor"
    splatlings_dct["nautilus 47"]["special"] = "ink storm"
    splatlings_dct["nautilus 47"]["points"] = 0
    splatlings_dct["nautilus 47"]["range"] = 74
    splatlings_dct["nautilus 47"]["role"] = "anchor, slayer"
    splatlings_dct["nautilus 47"]["weight"] = "middle"
    splatlings_dct["nautilus 47"]["charge speed"] = 37
    splatlings_dct["nautilus 47"]["mobility"] = 70
    splatlings_dct["nautilus 47"]["special points"] = 190

    splatlings_dct["zink mini splatling"]["sub"] = "toxic mist"
    splatlings_dct["zink mini splatling"]["special"] = "big bubbler"
    splatlings_dct["zink mini splatling"]["points"] = 0
    splatlings_dct["zink mini splatling"]["range"] = 62
    splatlings_dct["zink mini splatling"]["role"] = "support"
    splatlings_dct["zink mini splatling"]["weight"] = "middle"
    splatlings_dct["zink mini splatling"]["charge speed"] = 80
    splatlings_dct["zink mini splatling"]["mobility"] = 90
    splatlings_dct["zink mini splatling"]["special points"] = 200

    return splatlings_dct


def build_stringers() -> dict:
    """
    Creates the stringer dictionary
    class specifics: charge speed, mobility
    :return: the stringer dictionary
    """
    stringers = ["inkline tri-stringer", "reef-lux 450", "reef-lux 450 deco", "tri-stringer"]

    stringers_dct = dict()
    for stringer in stringers:
        stringers_dct[stringer] = dict()

    stringers_dct["spec A"] = ("charge speed", 3)
    stringers_dct["spec B"] = ("mobility", 3)

    stringers_dct["inkline tri-stringer"]["sub"] = "sprinkler"
    stringers_dct["inkline tri-stringer"]["special"] = "super chump"
    stringers_dct["inkline tri-stringer"]["points"] = 0
    stringers_dct["inkline tri-stringer"]["range"] = 88
    stringers_dct["inkline tri-stringer"]["role"] = "anchor, support"
    stringers_dct["inkline tri-stringer"]["weight"] = "middle"
    stringers_dct["inkline tri-stringer"]["charge speed"] = 40
    stringers_dct["inkline tri-stringer"]["mobility"] = 40
    stringers_dct["inkline tri-stringer"]["special points"] = 190

    stringers_dct["reef-lux 450"]["sub"] = "curling bomb"
    stringers_dct["reef-lux 450"]["special"] = "tenta missiles"
    stringers_dct["reef-lux 450"]["points"] = 0
    stringers_dct["reef-lux 450"]["range"] = 60
    stringers_dct["reef-lux 450"]["role"] = "slayer, support"
    stringers_dct["reef-lux 450"]["weight"] = "light"
    stringers_dct["reef-lux 450"]["charge speed"] = 75
    stringers_dct["reef-lux 450"]["mobility"] = 60
    stringers_dct["reef-lux 450"]["special points"] = 210

    stringers_dct["reef-lux 450 deco"]["sub"] = "splash wall"
    stringers_dct["reef-lux 450 deco"]["special"] = "reefslider"
    stringers_dct["reef-lux 450 deco"]["points"] = 0
    stringers_dct["reef-lux 450 deco"]["range"] = 60
    stringers_dct["reef-lux 450 deco"]["role"] = "slayer, support"
    stringers_dct["reef-lux 450 deco"]["weight"] = "light"
    stringers_dct["reef-lux 450 deco"]["charge speed"] = 75
    stringers_dct["reef-lux 450 deco"]["mobility"] = 60
    stringers_dct["reef-lux 450 deco"]["special points"] = 200

    stringers_dct["tri-stringer"]["sub"] = "toxic mist"
    stringers_dct["tri-stringer"]["special"] = "killer wail 5.1"
    stringers_dct["tri-stringer"]["points"] = 0
    stringers_dct["tri-stringer"]["range"] = 88
    stringers_dct["tri-stringer"]["role"] = "anchor, support"
    stringers_dct["tri-stringer"]["weight"] = "middle"
    stringers_dct["tri-stringer"]["charge speed"] = 40
    stringers_dct["tri-stringer"]["mobility"] = 40
    stringers_dct["tri-stringer"]["special points"] = 190

    return stringers_dct
