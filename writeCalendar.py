from pathlib import Path
from icalendar import Calendar, Event, vText
from datetime import datetime, timezone, tzinfo
from pytz import timezone
import re
import os
import json

cal = Calendar()

months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

def parseDate(date_str):
    tokenized_date = date_str.split(",")
    year = int(tokenized_date[2])
    # tokenizes month and date
    # ex: ['','Apr', '16']
    tokenized_mon_dd = tokenized_date[1].split(" ")
    month = tokenized_mon_dd[1]
    day = int(tokenized_mon_dd[2])

    return datetime(year, months[month], day, 0, 0, 0, 0, timezone("US/Eastern"))

def parseTime(time_str):
    tokenized_time = re.split("([0-9]+):([0-9]+)\ (AM|PM)", time_str)
    hh = int(tokenized_time[1])
    mm = int(tokenized_time[2])
    am_pm = tokenized_time[3]

    if (am_pm == "PM" and hh != 12):
        hh += 12
    elif (hh == 12 and am_pm == "AM"):
        hh = 0

    return hh, mm

cal = Calendar()

def writeToCalendar(row):
    event = Event()

    event.add("summary", "Shift")

    start_date = parseDate(row["Date"])
    hh, mm = parseTime(row["Shift Start"])
    start_date = start_date.replace(hour=hh, minute=mm)
    event.add("dtstart", start_date)

    end_date = parseDate(row["Date"])
    hh, mm = parseTime(row["Shift End"])
    end_date = end_date.replace(hour=hh, minute=mm)
    event.add("dtend", end_date)

    f = open("options.json")
    options = json.load(f)
    
    event["location"] = vText(options["worklocation"])

    # Add event to calenar
    cal.add_component(event)

    return

def save():
    directory = str(Path(__file__).parent) + "/output"
    print("ics file will be outputted to ", directory)

    f = open(os.path.join(directory, "hours.ics"), "wb")
    f.write(cal.to_ical())
    f.close()

    return