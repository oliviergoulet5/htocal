# htocal
This python script can duplicate your work schedule from a CSV file to an Apple Calendar.

![img](https://imgur.com/UorHPgH.png)

**Disclaimer**: I simply made this script for myself but I felt like I should share it. I did not create it to fit many different use cases, such as 24h time. 
Perhaps in the future I could add customizability to it.

### How to use
1. Run `htocal` from its directory. You must specify the CSV file as its command line argument.

For example: `htocal hours.csv`

2. This command will generate an ICS file which will appear in the output directory within the htocal directory.

3. Open the ICS file to add it to Apple's Calendar app.

### Constraints
Your CSV must have the following columns:
#### Date
The format of the "Date" column must be `Day, Mon, dd, yyyy`.

For example: Sat, Apr 2, 2022

#### Shift Start
This column is the time that your shift starts. It needs to be in 12h format.

#### Shift End
This column is the time that your shift ends. It needs to be in 12h format.

### Applications
I find that creating Excel files to track my hours and pay is more powerful, quick, and convenient over the user interface of Apple Calendar. I export the Excel file to a CSV after logging my hours and run `htocal`. This allows me to mirror my spreadsheet with my calendar. Afterwards, I use iOS Shortcuts to automate my alarms to go off 2 hours before any shift.

