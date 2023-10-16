# L.M. Garvey, 2023

# helper file for main.py to update an existing splatoon weapons spreadsheet

#
# the dictionaries used to select a class and weapon to update
#
blasters_dct = {"A": "blaster", "B": "clash blaster", "C": "clash blaster neo", "D": "luna blaster",
                "E": "luna blaster neo", "F": "range blaster", "G": "rapid blaster", "H": "rapid blaster deco",
                "I": "rapid blaster pro", "J": "rapid blaster pro deco", "K": "s-blast '92", "Z": "DONE"}

brellas_dct = {"A": "sorella brella", "B": "splat brella", "C": "tenta brella",
               "D": "tenta sorella brella", "E": "undercover brella", "Z": "DONE"}

brushes_dct = {"A": "inkbrush", "B": "inkbrush nouveau", "C": "octobrush",
               "D": "octobrush nouveau", "E": "painbrush", "Z": "DONE"}

chargers_dct = {"A": "bamboozler 14 mk I", "B": "classic squiffer", "C": "custom goo tuber",
                "D": "e-liter 4k", "E": "e-liter 4k scope", "F": "goo tuber", "G": "snipewriter 5h",
                "H": "splat charger", "I": "splatterscope", "J": "z+f splat charger",
                "K": "z+f splatterscope", "Z": "DONE"}

dualies_dct = {"A": "custom dualie squelchers", "B": "dapple dualies", "C": "dapple dualies nouveau",
               "D": "dark tetra dualies", "E": "dualie squelchers", "F": "glooga dualies",
               "G": "light tetra dualies", "H": "splat dualies", "Z": "DONE"}

rollers_dct = {"A": "big swig roller", "B": "big swig roller express", "C": "carbon roller",
               "D": "carbon roller deco", "E": "dynamo roller", "F": "flingza roller",
               "G": "gold dynamo roller", "H": "krak-on splat roller", "I": "splat roller", "Z": "DONE"}

shooters_dct = {"A": ".52 gal", "B": ".96 gal", "C": ".96 gal deco", "D": "aerospray mg", "E": "aerospray rg",
                "F": "annaki splattershot nova", "G": "custom jet squelcher", "H": "custom splattershot jr",
                "I": "forge splattershot pro", "J": "h-3 nozzlenose", "K": "h-3 nozzlenose d", "L": "hero shot replica",
                "M": "jet squelcher", "N": "l-3 nozzlenose", "O": "l-3 nozzlenose d", "P": "n-zap '85",
                "Q": "n-zap '89", "R": "neo splash-o-matic", "S": "neo sploosh-o-matic", "T": "splash-o-matic",
                "U": "splattershot", "V": "splattershot jr", "W": "splattershot nova", "X": "splattershot pro",
                "Y": "sploosh-o-matic", "AA": "squeezer", "BB": "tentatek splattershot", "Z": "DONE"}

sloshers_dct = {"A": "bloblobber", "B": "bloblobber deco", "C": "dread wringer", "D": "explosher", "E": "slosher",
                "F": "slosher deco", "G": "sloshing machine", "H": "sloshing machine neo", "I": "tri-slosher",
                "J": "tri-slosher nouveau", "Z": "DONE"}

splatanas_dct = {"A": "splatana stamper", "B": "splatana wiper", "C": "splatana wiper deco", "Z": "DONE"}

splatlings_dct = {"A": "ballpoint splatling", "B": "ballpoint splatling nouveau", "C": "heavy edit splatling",
                  "D": "heavy splatling", "E": "heavy splatling deco", "F": "hydra splatling",
                  "G": "mini splatling", "H": "nautilus 47", "I": "zink mini splatling", "Z": "DONE"}

stringers_dct = {"A": "inkline tri-stringer", "B": "reef-lux 450", "C": "tri-stringer", "Z": "DONE"}

pick_class = {"A": "blaster", "B": "brella", "C": "brush", "D": "charger", "E": "dualies", "F": "roller",
              "G": "shooter", "H": "slosher", "I": "splatana", "J": "splatling", "K": "stringer",
              "Z": "DONE"}

classes_dct = {"A": blasters_dct, "B": brellas_dct, "C": brushes_dct, "D": chargers_dct, "E": dualies_dct,
               "F": rollers_dct, "G": shooters_dct, "H": sloshers_dct, "I": splatanas_dct, "J": splatlings_dct,
               "K": stringers_dct, "Z": "DONE"}


def update_weapon(book, book_name, weapon) -> None:
    """
    Updates the weapon in the given class with the given points
    :param book: opened workbook object to update in
    :param book_name: name of workbook to update in
    :param weapon: name of weapon to update
    :return: None
    """
    sheet = book["numbers"]

    print("Please enter your current points for {}\n".format(weapon))
    points = int(input())
    if points < 0:
        points = 0
    if points > 1160000:
        points = 1160000
    for row in range(2, 103):
        if sheet.cell(row, 2).value == weapon:
            sheet.cell(row, 6).value = points
            print("Successfully set {} to have {} points.\n".format(weapon, points))
            book.save(book_name)
            return


def update_wrapper(book, book_name) -> None:
    """
    Updates point values in an existing sheet
    :param book: opened workbook object to update
    :param book_name: name of workbook to update
    :return: None
    """

    while True:
        print("Select a weapon class to update:\n")
        for class_opt, class_name in pick_class.items():
            print("{}: {}\n".format(class_opt, class_name))
        class_opt = input().upper()
        if class_opt == "Z":
            print("Finished updating.\n")
            break

        if class_opt not in pick_class.keys():
            print("Please only type the letter option of the class.\n")
            continue

        class_name = pick_class[class_opt]
        class_dct = classes_dct[class_opt]

        print("Select a {} to update:\n".format(class_name))
        for letter, name in class_dct.items():
            print("{}: {}\n".format(letter, name))
        weapon = input().upper()
        if weapon not in class_dct.keys():
            print("Please only type the letter option of the weapon.\n")
        elif weapon == "Z":
            print("Finished updating.\n")
            break
        else:
            update_weapon(book, book_name, class_dct[weapon])
