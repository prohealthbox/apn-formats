import json, sqlite3, unicodedata

with open("regex.json", "r") as formats:
    regex = json.load(formats)
    ct = regex["CT"]
    conn = sqlite3.connect('../apn.db')
    sql = "insert into apn(apn_format, apn_regex, county, state, state_abbrev) values(?, ?, ?, ?, ?)"
    cur = conn.cursor()

    for county, values in ct.iteritems():
        for i in range(0, len(values["formats"])):
            cur.execute(sql, (values["formats"][i], values["regex"][i], county, "Connecticut", "CT"))
    conn.commit()
