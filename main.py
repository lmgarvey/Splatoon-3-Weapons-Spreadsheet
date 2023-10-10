# L.M. Garvey, 2023

# program to create a splatoon 3 weapons spreadsheet
# uses Workbook from openpyxl
# the spreadsheet will be stylized to all lowercase, and saved in the same directory as this program
# https://github.com/lmgarvey/Splatoon-3-Weapons-Spreadsheet

# takes as input from user: 'current points' for a prompted weapon
#       you can check this number by clicking ZR twice with the
#       specified weapon selected in-game and looking at the
#       number in the bar graph (your 'freshness' for that weapon).
#       each weapon will be prompted individually. as of october 2023,
#       there are 101 weapons.
# using this, produces a spreadsheet with several sheets:
#       1. the `numbers` sheet, including progress toward the next
#          freshness, as well as several default values, such as
#          each weapon's sub and special, range, and more.
#       2. the basic chart calculations, which performs calculations
#          based on the user's inputs to the `numbers` sheet to create
#          pie charts showing where they've earned most of their points,
#          in terms of weapon class, subs, specials, and more.
#       3. the basic pie charts, based on the calculations made in the
#          directly previous sheet.
#       4. chart calculations, but only for weapons with less than five
#          stars. there are 1 million points between four and five stars,
#          so it is valuable to remove those outliers.
#       5. pie charts for weapons with less than five stars, again based
#          on the calculations made in the directly previous sheet.
# for the class-specific values, such as impact, damage, ink speed,
#          charge speed, the value will be in its appropriate column, and
#          the corresponding chart will be in the cell directly to the right.
#          to keep this consistent, column W is titled 'mobility chart' to
#          hold the charts for the mobility numbers.

# future plans/ideas:
# automate creating calculations and charts for less than
#       four stars, <3, <2, <1, by generalizing the <5 process
# calculations and charts for non-unique things, eg shooter ranges vs charger ranges
#       and which subs are more common to certain classes
# have an option of create vs update, eg mass-changing points
#       so if they want to have the program go through and change,
#       you can have a "while (taking input): getclass, getweapon, getpoints, update"
# matchmaking numbers across classes


from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.formatting.rule import DataBarRule


def set_up_blasters(blasters: list) -> dict:
    """
    Creates blaster class dictionary:
    {weapon:
        {sub: name of sub}
        {special: name of special}
        {points: current freshness points}
        {range: range as a number}
        {role: role(s)}
        {weight: light, middle, or heavy}
        {impact: impact as a number}
        {fire rate: fire rate as a number}
    }
    :param blasters: list of all weapons in the blaster class
    :return: the blaster dictionary
    """
    blaster_dct = dict()
    for blaster in blasters:
        blaster_dct[blaster] = dict()

    blaster_dct["blaster"]["sub"] = "autobomb"
    blaster_dct["blaster"]["special"] = "big bubbler"
    blaster_dct["blaster"]["points"] = 0
    blaster_dct["blaster"]["range"] = 27
    blaster_dct["blaster"]["role"] = "slayer"
    blaster_dct["blaster"]["weight"] = "middle"
    blaster_dct["blaster"]["impact"] = 70
    blaster_dct["blaster"]["fire rate"] = 20

    blaster_dct["clash blaster"]["sub"] = "splat bomb"
    blaster_dct["clash blaster"]["special"] = "trizooka"
    blaster_dct["clash blaster"]["points"] = 0
    blaster_dct["clash blaster"]["range"] = 21
    blaster_dct["clash blaster"]["role"] = "skirmisher, slayer"
    blaster_dct["clash blaster"]["weight"] = "light"

    blaster_dct["clash blaster neo"]["sub"] = "curling bomb"
    blaster_dct["clash blaster neo"]["special"] = "super chump"
    blaster_dct["clash blaster neo"]["points"] = 0
    blaster_dct["clash blaster neo"]["range"] = 21
    blaster_dct["clash blaster neo"]["role"] = "slayer, support"
    blaster_dct["clash blaster neo"]["weight"] = "light"

    blaster_dct["luna blaster"]["sub"] = "splat bomb"
    blaster_dct["luna blaster"]["special"] = "zipcaster"
    blaster_dct["luna blaster"]["points"] = 0
    blaster_dct["luna blaster"]["range"] = 18
    blaster_dct["luna blaster"]["role"] = "slayer, support"
    blaster_dct["luna blaster"]["weight"] = "light"

    blaster_dct["luna blaster neo"]["sub"] = "fizzy bomb"
    blaster_dct["luna blaster neo"]["special"] = "ultra stamp"
    blaster_dct["luna blaster neo"]["points"] = 0
    blaster_dct["luna blaster neo"]["range"] = 18
    blaster_dct["luna blaster neo"]["role"] = "slayer, support"
    blaster_dct["luna blaster neo"]["weight"] = "light"

    blaster_dct["range blaster"]["sub"] = "suction bomb"
    blaster_dct["range blaster"]["special"] = "wave breaker"
    blaster_dct["range blaster"]["points"] = 0
    blaster_dct["range blaster"]["range"] = 56
    blaster_dct["range blaster"]["role"] = "slayer, support"
    blaster_dct["range blaster"]["weight"] = "middle"

    blaster_dct["rapid blaster"]["sub"] = "ink mine"
    blaster_dct["rapid blaster"]["special"] = "triple inkstrike"
    blaster_dct["rapid blaster"]["points"] = 0
    blaster_dct["rapid blaster"]["range"] = 62
    blaster_dct["rapid blaster"]["role"] = "slayer"
    blaster_dct["rapid blaster"]["weight"] = "middle"

    blaster_dct["rapid blaster deco"]["sub"] = "torpedo"
    blaster_dct["rapid blaster deco"]["special"] = "inkjet"
    blaster_dct["rapid blaster deco"]["points"] = 0
    blaster_dct["rapid blaster deco"]["range"] = 62
    blaster_dct["rapid blaster deco"]["role"] = "slayer"
    blaster_dct["rapid blaster deco"]["weight"] = "middle"

    blaster_dct["rapid blaster pro"]["sub"] = "toxic mist"
    blaster_dct["rapid blaster pro"]["special"] = "ink vac"
    blaster_dct["rapid blaster pro"]["points"] = 0
    blaster_dct["rapid blaster pro"]["range"] = 72
    blaster_dct["rapid blaster pro"]["role"] = "anchor, support"
    blaster_dct["rapid blaster pro"]["weight"] = "middle"

    blaster_dct["rapid blaster pro deco"]["sub"] = "angle shooter"
    blaster_dct["rapid blaster pro deco"]["special"] = "killer wail 5.1"
    blaster_dct["rapid blaster pro deco"]["points"] = 0
    blaster_dct["rapid blaster pro deco"]["range"] = 72
    blaster_dct["rapid blaster pro deco"]["role"] = "anchor, support"
    blaster_dct["rapid blaster pro deco"]["weight"] = "middle"

    blaster_dct["s-blast '92"]["sub"] = "sprinkler"
    blaster_dct["s-blast '92"]["special"] = "reefslider"
    blaster_dct["s-blast '92"]["points"] = 0
    blaster_dct["s-blast '92"]["range"] = 45
    blaster_dct["s-blast '92"]["role"] = "slayer"
    blaster_dct["s-blast '92"]["weight"] = "middle"

    return blaster_dct


def set_up_weapons() -> dict:
    """
    Sets up all the weapons alphabetically within their own classes
    Defaults each weapon to have zero points
    :return: dict of {class:
                        {weapon_in_class: 0}
                        }
    """
    blasters = ["blaster", "clash blaster", "clash blaster neo", "luna blaster", "luna blaster neo",
               "range blaster", "rapid blaster", "rapid blaster deco", "rapid blaster pro",
               "rapid blaster pro deco", "s-blast '92"]
    brella = ["sorella brella", "splat brella", "tenta brella", "tenta sorella brella", "undercover brella"]
    brush = ["inkbrush", "inkbrush nouveau", "octobrush", "octobrush noueavu", "painbrush"]
    charger = ["bamboozler 14 mk I", "classic squiffer", "custom goo tuber", "e-liter 4k", "e-liter 4k scope",
               "goo tuber", "snipewriter 5h", "splat charger", "splatterscope", "z+f splat charger",
               "z+f splatterscope"]
    dualies = ["custom dualie squelchers", "dapple dualies", "dapple dualies nouveau", "dark tetra dualies",
               "dualie squelchers", "glooga dualies", "light tetra dualies", "splat dualies"]
    roller = ["big swig roller", "big swig roller express", "carbon roller", "carbon roller deco",
              "dynamo roller", "flingza roller", "gold dynamo roller", "krak-on splat roller", "splat roller"]
    shooter = [".52 gal", ".96 gal", ".96 gal deco", "aerospray mg", "aerospray rg", "annaki splattershot nova",
               "custom jet squelcher", "custom splattershot jr", "forge splattershot pro", "h-3 nozzlenose",
               "h-3 nozzlenose d", "hero shot replica", "jet squelcher", "l-3 nozzlenose", "l-3 nozzlenose d",
               "n-zap '85", "n-zap '89", "neo splash-o-matic", "neo sploosh-o-matic", "splash-o-matic",
               "splattershot", "splattershot jr", "splattershot nova", "splattershot pro", "sploosh-o-matic",
               "squeezer", "tentatek splattershot"]
    slosher = ["bloblobber", "bloblobber deco", "dread wringer", "explosher", "slosher", "slosher deco",
               "sloshing machine", "sloshing machine neo", "tri-slosher", "tri-slosher noueavu"]
    splatana = ["splatana stamper", "splatana wiper", "splatana wiper deco"]
    splatling = ["ballpoint splatling", "ballpoint splatling nouveau", "heavy edit splatling", "heavy splatling",
                 "heavy splatling deco", "hydra splatling", "mini splatling", "nautilus 47", "zink mini splatling"]
    stringer = ["inkline tri-stringer", "reef-lux 450", "tri-stringer"]

    blaster_dct = set_up_blasters(blasters)


    brella_dct = dict.fromkeys(brella, 0)
    brush_dct = dict.fromkeys(brush, 0)
    charger_dct = dict.fromkeys(charger, 0)
    dualies_dct = dict.fromkeys(dualies, 0)
    roller_dct = dict.fromkeys(roller, 0)
    shooter_dct = dict.fromkeys(shooter, 0)
    slosher_dct = dict.fromkeys(slosher, 0)
    splatana_dct = dict.fromkeys(splatana, 0)
    splatling_dct = dict.fromkeys(splatling, 0)
    stringer_dct = dict.fromkeys(stringer, 0)

    out = {"blaster": blaster_dct, "brella": brella_dct, "brush": brush_dct, "charger": charger_dct,
           "dualies": dualies_dct, "roller": roller_dct, "shooter": shooter_dct, "slosher": slosher_dct,
           "splatana": splatana_dct, "splatling": splatling_dct, "stringer": stringer_dct}
    return out


def collect_points(dct: dict, default_zeros=False) -> None:
    """
    Outer function that calls collect_points for each class in dct
    :param dct: {class:
                    {weapon_in_class: points}
                 }
    :param default_zeros:
        True: fill all weapon points with zero
        False: prompt user for their points
    :return: None
    """
    for weapon_class in dct:
        if not default_zeros:
            print("\n")
            print("{} class!".format(weapon_class))

        for weapon in dct[weapon_class]:
            if not default_zeros:
                print("Current points for '{}', or 'q' to quit:".format(weapon))
                points = input()
                if points == "q" or points == "Q":
                    default_zeros = True
                    points = 0
                    print("Stopping points collection, filling in remaining weapons with zero points.\n")
                else:
                    try:
                        points = int(points)
                    except ValueError:
                        print("Invalid points number, settings points = 0.\n")
                        points = 0
            else:
                points = 0
            if not points or points < 0:
                points = 0
            if points > 1160000:
                points = 1160000
            dct[weapon_class][weapon] = points

        if not default_zeros:
            print("~~~~~~~~~~")


def set_header_row(sheet) -> None:
    """
    Sets up the header row
    :param sheet: sheet to set the header row on
    :return: None
    """
    sheet["A1"] = "class"
    sheet["B1"] = "weapon"
    sheet["C1"] = "sub"
    sheet["D1"] = "special"
    sheet["E1"] = "freshness"
    sheet["F1"] = "current"
    sheet["G1"] = "checkpoint"
    sheet["H1"] = "necessary"
    sheet["I1"] = "progress (%)"
    sheet["J1"] = "progress (chart)"
    sheet["K1"] = "range (#)"
    sheet["L1"] = "range (chart)"
    sheet["M1"] = "role"
    sheet["N1"] = "weight/speed"
    sheet["O1"] = "impact"
    sheet["P1"] = "damage"
    sheet["Q1"] = "ink speed"
    sheet["R1"] = "charge speed"
    sheet["S1"] = "fire rate"
    sheet["T1"] = "durability"
    sheet["U1"] = "handling"
    sheet["V1"] = "mobility"
    sheet["W1"] = "mobility chart"
    sheet["X1"] = "special points"


def set_up_sheet(sheet, weapons) -> None:
    """
    Sets up basic outline of sheet - column headers,
    class names, and weapon names
    :param sheet: sheet to set up
    :param weapons: {class:
                        {weapon: points}
                     }
    :return: None
    """
    set_header_row(sheet)

    # set up class and weapon names in columns A and B
    start = 2
    for weapon_class in weapons:

        # for getting each weapon into its own cell
        weapons_dct_as_lst = list()
        for weapon in weapons[weapon_class]:
            weapons_dct_as_lst.append(weapon)

        end = len(weapons[weapon_class]) + start
        for row in range(start, end):
            # set weapon class in column A
            sheet.cell(row, 1).value = weapon_class

            # set weapon name in column B and point value in column F
            weapon = weapons_dct_as_lst[row - start]
            sheet.cell(row, 2).value = weapon
            sheet.cell(row, 6).value = weapons[weapon_class][weapon]

        start = end

    #
    # formatting!
    #

    # weapon class, weapon name, and column header always visible:
    sheet.freeze_panes = "C2"

    # header row in bold
    for cell in sheet[1]:
        cell.font = Font(bold=True)

    # match width to widest cell in column
    # https://stackoverflow.com/a/35790441
    dims = dict()
    for row in sheet.rows:
        for cell in row:
            if cell.value:
                dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
    for col, val in dims.items():
        sheet.column_dimensions[col].width = val


def set_up_points_columns(sheet) -> None:
    """
    Modifies points-related columns:
        E: freshness in stars
        G: next freshness checkpoint
        H: points remaining to next checkpoint
        I: progress to next checkpoint as a percentage
        J: progress to next checkpoint as a bar chart
    User's points are held in column F
    :param sheet: sheet to modify
    :param weapons: {class:
                        {weapon: points}
                     }
    :return: None
    """

    for row in range(2, 103):
        # E: freshness in stars
        sheet.cell(row, 5).value = "=IF(F{} < 10000, \"☆\", " \
                                   "IF(F{} < 25000, \"★\", " \
                                   "IF(F{} < 60000, \"★★\", " \
                                   "IF(F{} < 160000, \"★★★\", " \
                                   "IF(F{} < 1160000, \"★★★★\", \"★★★★★\")))))" \
            .format(row, row, row, row, row)

        # G: next freshness checkpoint
        sheet.cell(row, 7).value = "=IF(F{} < 10000, 10000, " \
                                   "IF(F{} < 25000, 25000, " \
                                   "IF(F{} < 60000, 60000, " \
                                   "IF(F{} < 160000, 160000, " \
                                   "IF(F{} < 1160000, 1160000, 1160000)))))" \
            .format(row, row, row, row, row)

        # H: points remaining to next checkpoint
        sheet.cell(row, 8).value = "=G{} - F{}".format(row, row)

        # I: progress to next checkpoint as a percentage
        sheet.cell(row, 9).value = "=F{} * 100 / G{}".format(row, row)

        # J: progress as bar chart, need the numbers in there first...
        sheet.cell(row, 10).value = "=F{} * 100 / G{}".format(row, row)

    # ...J again: hide the numbers, replace them with a data bar
    rule = DataBarRule(start_type='num', start_value=0, end_type='num', end_value=100,
                       color="000000", showValue=False)
    sheet.conditional_formatting.add('J2:J102', rule)


if __name__ == '__main__':
    print("Welcome to `Creating your Splatoon 3 weapons spreadsheet!`\n")
    print()
    print("This program will prompt you with one weapon at a time, and ask for your current points on that weapon.\n")
    print("Type the relevant number when prompted, then press `enter`. Repeat this for all 101 weapons.\n"
          "If you do not have the prompted weapon, you can type `0`, or just press `enter` with no input.\n"
          "The weapons will be prompted by class, and alphabetically within that class.\n"
          "If at any time you wish to stop, type 'q', and all remaining weapons will be defaulted to zero points.\n")
    print()
    print("At this time, you can choose to (A) fill in your points, or (B) have a spreadsheet created \n"
          "with all of the point values defaulted to zero. If you select (A), you may also type `q` at any\n"
          "time to stop, and have the remaining weapons all defaulted to zero.\n"
          "Please enter your selection:\n")
    choice = input()
    while choice.upper() != "A" and choice.upper() != "B":
        print("Sorry, please make sure you type only A, a, B, or b.\n"
              "A: Fill in your own point values\n"
              "B: Default all values to zero\n")
        choice = input()

    default_to_zeros = False
    if choice.upper() == "B":
        default_to_zeros = True

    workbook = Workbook()
    numbers_sheet = workbook.active
    numbers_sheet.title = "numbers"

    # {class: {weapon : 0} }
    weapons_dct = set_up_weapons()
    collect_points(weapons_dct, default_to_zeros)
    set_up_sheet(numbers_sheet, weapons_dct)
    set_up_points_columns(numbers_sheet)

    # in the future when there's more happening than just points, i would like to do:

    # class:
    # weapon: sub, special, points, range, role, weight/speed

    # or alternatively,
    # weapon: {sub: name}, {special: name}, {points: number}, ...

    # blasters:
    # weapon: impact, fire rate
    # [class]:
    # weapon: [class specific 1], [class specific 2]

    workbook.save(filename="splatoon_weapons.xlsx")

    print()
    print("Done!")

    formulas_sheet = workbook.create_sheet("formulas")
