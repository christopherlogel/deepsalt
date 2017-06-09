# -----------------------------------------------------------------------------
# Name:        deep_salt.py
# Purpose:     This is the main Deep Salt script
#
# Author:      Christopher Logel
#
# Created:     6/9/2017
# Copyright:   (c) Christopher Logel
# -----------------------------------------------------------------------------

# Imports
import pickle

match_list = pickle.load(open("match_data.p", "rb"))

print match_list[0]