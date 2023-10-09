# Splatoon-3-Weapons-Spreadsheet
Simple program to take user input and create a spreadsheet of usage across all Splatoon 3 weapons.

This program will prompt the user to provide their freshness points for each weapon available in Splatoon 3. It will create an excel spreadsheet based on that information, which contains multiple sheets within it: The main sheet of simple numbers, a sheet of formulas, and a sheet of pie charts created from those formulas.

*TK - In the future, I would like to have an option to either create a new sheet, or update a pre-existing one as needed, with prompts for class -> weapon within that class -> "here is your current value, please enter your new value" as needed. In the meantime, it only creates a new sheet.


![freshnessimg](https://github.com/lmgarvey/Splatoon-3-Weapons-Spreadsheet/assets/94126547/38fa66fa-bb74-4a43-b681-24e30a763899)

On running the program, the console will print a brief explanation of the process, then prompt you for your current points on a certain weapon. In the image above, note the bar at the top-right reading "19400 / 25000", with a single filled-in star above it. "19400" is the number of points the user has, and is the number in question when the user is prompted at the console for their current points. "25000" is the number of total points the user needs to reach the next freshness checkpoint, and the single star means the user has reached the first freshness checkpoint.

The console will run through each class alphabetically, and each weapon within that class alphabetically. This is for ease of use on the user's part, as weapons can be sorted by class if you click the 'L' stick while in the weapon select menu. This massively narrows down the number of weapons the user needs to look through when finding the console-prompted current points.

For example, it will first prompt for weapons in the 'blaster' class, beginning with the blaster, then the clash blaster, then the clash blaster neo, and so on. Once it has prompted all of the blasters, it will prompt for 'brellas', beginning with the sorella brella, then the splat brella. This continues for all the weapons in all the classes. Once all of the points have been provided, the program will create a .xlsx spreadsheet, and save it to the same directory the program is running in.
