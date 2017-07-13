# -----------------------------------------------------------------------------
# Name:        data_processor.py
# Purpose:     Pull data from spreadsheet and preprocesses it
#
# Author:      Christopher Logel
#
# Created:     6/10/2017
# Copyright:   (c) Christopher Logel
# -----------------------------------------------------------------------------


import xlrd
import pickle

workbook = xlrd.open_workbook("hero_vals.xlsx")
sheet = workbook.sheet_by_index(0)

# Create the hero list
heroes = list()

# Build the list
for i in range(1, 114):
    # Grab the hero's row & init a list for the hero
    row = sheet.row(i)
    hero = list()

    # Build the hero's list
    hero.append(row[0].value.encode("ascii", "ignore"))

    for j in range(2, 11):
        hero.append(row[j].value)

    # Add the hero list to the big list
    heroes.insert(int(row[1].value), hero)

# Save the hero data
pickle.dump(heroes, open("hero_list.p", "wb"))
