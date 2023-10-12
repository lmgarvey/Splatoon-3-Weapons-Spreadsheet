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

import build_weapons


def set_up_weapons() -> dict:
    """
    Sets up all the weapons alphabetically within their own classes
    Defaults each weapon to have zero points
    Calls build_[class] for each class in build_weapons.py
    :return: dict of
                    {class:
                        {
                        spec A: ( name of class specific A, offset from first spec A column as 0-3 )
                        spec B: ( name of class specific B, offset from first spec B column as 0-3 )
                        weapon_in_class:
                            {
                            sub: name of sub
                            special: name of special
                            points: current freshness points
                            range: range as a number
                            role: role(s)
                            weight: light, middle, or heavy
                            class_specific_1: value as number
                            class_specific_2: value as number
                            special points: points needed for special
                            }
                        }
                    }
    """

    blaster_dct = build_weapons.build_blasters()
    brella_dct = build_weapons.build_brellas()
    brush_dct = build_weapons.build_brushes()
    charger_dct = build_weapons.build_chargers()
    dualies_dct = build_weapons.build_dualies()
    roller_dct = build_weapons.build_rollers()
    shooter_dct = build_weapons.build_shooters()
    slosher_dct = build_weapons.build_sloshers()
    splatana_dct = build_weapons.build_splatanas()
    splatling_dct = build_weapons.build_splatlings()
    stringer_dct = build_weapons.build_stringers()

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
            if weapon == "spec A" or weapon == "spec B":
                continue
            if not default_zeros:
                print("Current points for '{}', or 'q' to quit:".format(weapon))
                points = input()
                if points.upper() == "Q":
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
            points = 123000  # TK
            dct[weapon_class][weapon]["points"] = points

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
        class names, weapon names, subs, specials,
        default zero points, range, role, weight,
        class-spec-A, class-spec-B, points for special
    :param sheet: sheet to set up
    :param weapons: {class:
                        {
                        spec A: (name of class spec A, offset from first spec A column)
                        spec B: (name of class spec B, offset from first spec B column)
                        weapon: dict of attribute : value
                        }
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
            if weapon != "spec A" and weapon != "spec B":
                weapons_dct_as_lst.append(weapon)

        class_spec_1 = weapons[weapon_class]["spec A"][0]
        class_spec_2 = weapons[weapon_class]["spec B"][0]
        spec_1_offset = weapons[weapon_class]["spec A"][1]
        spec_2_offset = weapons[weapon_class]["spec B"][1]

        end = len(weapons[weapon_class]) + start - 2  # -2 handles the spec_A and spec_B items
        for row in range(start, end):
            # set weapon class in column A
            sheet.cell(row, 1).value = weapon_class

            weapon = weapons_dct_as_lst[row - start]
            sheet.cell(row, 2).value = weapon  # column B
            sheet.cell(row, 3).value = weapons[weapon_class][weapon]["sub"]  # C
            sheet.cell(row, 4).value = weapons[weapon_class][weapon]["special"]  # D
            sheet.cell(row, 6).value = weapons[weapon_class][weapon]["points"]  # F
            sheet.cell(row, 11).value = weapons[weapon_class][weapon]["range"]  # K
            sheet.cell(row, 13).value = weapons[weapon_class][weapon]["role"]  # M
            sheet.cell(row, 14).value = weapons[weapon_class][weapon]["weight"]  # N
            sheet.cell(row, 15 + spec_1_offset).value = weapons[weapon_class][weapon][class_spec_1]  # O, P, Q, R
            sheet.cell(row, 19 + spec_2_offset).value = weapons[weapon_class][weapon][class_spec_2]  # S, T, U, V
            sheet.cell(row, 24).value = weapons[weapon_class][weapon]["special points"]  # X

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
        sheet.column_dimensions[col].width = val + 3


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


def set_up_cell_charts(sheet) -> None:
    """
    Sets up the cell bar charts for range and class specific values:
        L: range as a chart
        P: impact as a chart (nominally 'damage (numbers)' column)
        Q: damage as a chart (nominally 'ink speed (numbers)' column)
        R: ink speed as a chart (nominally 'charge speed (numbers)' column)
        S: charge speed as a chart (nominally 'fire rate (numbers)' column)
        T: fire rate as a chart (nominally 'durability (numbers)' column)
        U: durability as a chart (nominally 'handling (numbers)' column)
        V: handling as a chart (nominally 'mobility (numbers)' column)
        W: mobility as a chart (named accordingly)
    :param sheet: sheet to set up charts on
    :return: None
    """
    # range's value and chart aren't contiguous with class specs, do it separately
    for row in range(2, 103):
        sheet.cell(row, 12).value = "=K{}".format(row)
    rule = DataBarRule(start_type='num', start_value=0, end_type='num', end_value=100,
                       color="000000", showValue=False)
    sheet.conditional_formatting.add('L2:L102', rule)

    # grab values from preceding column
    read_from_col = ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
    write_to_col =   [15,  16,  17,  18,  19,  20,  21,  22,  23]
    for i in range(1, len(read_from_col)):
        # read value from previous column
        # eg column P (16)'s value comes from column O (15)
        read_from = read_from_col[i-1]      # previous column we're reading from
        write_to = write_to_col[i]          # column to put it in
        check_val_col = write_to_col[i-1]   # for reading value from column-as-number
        for row in range(2, 103):
            # check if there IS a value to read from
            jinkies = sheet.cell(row, check_val_col).value
            jonkoes = sheet.cell(row, check_val_col - 1).value
            # if (value to read)   and  (two columns back is empty or is the weight column)
            if jinkies is not None and (jonkoes is None or type(jonkoes) == str):
                sheet.cell(row, write_to).value = "={}{}".format(read_from, row)

    # # turn values into charts: hide the numbers, replace with data bar
    charts_to_add = ['P2:P12', 'Q13:Q17', 'Q34:Q41', 'Q51:Q90', 'R18:R22', 'R42:R50',
                     'S23:S33', 'S91:S102', 'T2:T12', 'T51:T77', 'U13:U17', 'V18:V22',
                     'V42:V50', 'V78:V90', 'W23:W41', 'W91:W102']
    for column in charts_to_add:
        rule = DataBarRule(start_type='num', start_value=0, end_type='num', end_value=100,
                           color="000000", showValue=False)
        sheet.conditional_formatting.add(column, rule)


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
          "Please enter your selection:"
          " A: Create sheet and fill in your own point values\n"
          " B: Create sheet and default all points to zero\n"
          " C: Update an existing sheet (NOT WORKING YET)\n")
    # choice = input()
    choice = "B"  # TK
    while choice.upper() != "A" and choice.upper() != "B":
        print("Sorry, please make sure you type only A or B.\n"
              "A: Fill in your own point values\n"
              "B: Default all points to zero\n")
        choice = input()

    default_to_zeros = False
    if choice.upper() == "B":
        default_to_zeros = True

    workbook = Workbook()
    numbers_sheet = workbook.active
    numbers_sheet.title = "numbers"

    weapons_dct = set_up_weapons()
    collect_points(weapons_dct, default_to_zeros)
    set_up_sheet(numbers_sheet, weapons_dct)
    set_up_points_columns(numbers_sheet)

    # TK: in progress, charts mess up when you sort by anything other than class:weapon
    set_up_cell_charts(numbers_sheet)

    workbook.save(filename="splatoon_weapons.xlsx")

    print()
    print("Done!")

    formulas_sheet = workbook.create_sheet("formulas")
