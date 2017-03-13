import json


def main():
    jfile = json.load(open("regex.json", "r"))
    for state, value in jfile.iteritems():
        if state != "DC":
            for county, formats in value.iteritems():
                length = len(formats["regex"])
                if length > 0:
                    for i in range(0, length):
                        jfile[state][county]["regex"][i] = "^" + jfile[state][county]["formats"][i] + "$"

    with open("regex.json", "w") as jsonfile:
        json.dump(jfile, jsonfile)


if __name__ == "__main__":
    main()
