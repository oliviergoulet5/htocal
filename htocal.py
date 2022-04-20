#!/usr/bin/env python

import csv
from writeCalendar import writeToCalendar, save
import sys

def main(argv):
    file_name = str(argv)
    with open(file_name, mode = "r") as file:
        csvFile = csv.DictReader(file)

        for row in csvFile:
            writeToCalendar(row)
        
        save()

    return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You must provide a file to operate on.")
    else:
        main(sys.argv[1])