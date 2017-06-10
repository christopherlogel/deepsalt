# -----------------------------------------------------------------------------
# Name:        hero_miner.py
# Purpose:     Mines hero data from open dota
#
# Author:      Christopher Logel
#
# Created:     6/9/2017
# Copyright:   (c) Christopher Logel
# -----------------------------------------------------------------------------

# Imports
import urllib
import json
import pickle
import ast


# Grab data from opendota
data = json.load(urllib.urlopen("https://api.opendota.com/api/heroes"))

# Process data
for hero in data:
    hero["name"] = hero["localized_name"]
    hero.pop("localized_name", None)
    hero.pop("legs", None)

# Save data
pickle.dump(data, open("hero_list.p", "wb"))
