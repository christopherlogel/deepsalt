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

workbook = xlrd.open_workbook("hero_vals.xlsx")
ws = workbook.sheet_by_index(0)
