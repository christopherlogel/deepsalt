# -----------------------------------------------------------------------------
# Name:        data_miner.py
# Purpose:     This is the data mining tool for Deep Salt
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
import threading
import sys

# Import data from last session
match_list = pickle.load(open("match_data.p", "rb"))


def load_new_data():
    # If we have targeted number of matches, break
    if len(match_list) > int(sys.argv[1]):
        print "Finished receiving data."
        sys.exit()

    # Grab data from opendota
    data = json.load(urllib.urlopen("https://api.opendota.com/api/publicMatches"))

    # Add the new matches to the data set
    for match in data:
        if match not in match_list:
            match_list.append(match)

    # Print the current list length
    print "Number of unique matches: %d." % len(match_list)

    # Save data
    pickle.dump(match_list, open("match_data.p", "wb"))

    # Start new data pull
    threading.Timer(15, load_new_data).start()

# Run the script
load_new_data()