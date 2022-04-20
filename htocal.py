#!/usr/bin/env python

import csv
from writeCalendar import writeToCalendar, save
from changeOption import changeOption
from os import path
import shutil
import argparse

parser = argparse.ArgumentParser()

#-f FILE -wl LOCATION
parser.add_argument("-f", "--file", dest="file", help="CSV file")
parser.add_argument("-wl", "--worklocation", dest="worklocation", help="Work location")

args = parser.parse_args()

def main():
    if args.worklocation:
        changeOption("worklocation", args.worklocation)

    if args.file:
        file_name = args.file

        with open(file_name, mode = "r") as file:
            csvFile = csv.DictReader(file)

            if not path.exists("options.json"):
                shutil.copy("defaultOptions.json", "options.json")

            for row in csvFile:
                writeToCalendar(row)
            
            save()

    return


if __name__ == "__main__":
    main()
