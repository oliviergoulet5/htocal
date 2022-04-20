import json

def changeOption(option, value):
    with open("options.json", "r+") as f:
        options = json.load(f)
        options[option] = value
        f.seek(0)
        json.dump(options, f, indent=4)
        f.truncate()