import re
from apn import lookup

states = (
    'Washington', 'Delaware', 'District of Columbia', 'Wisconsin', 'West Virginia', 'Hawaii', 'Florida', 'Wyoming',
    'New Hampshire', 'New Jersey', 'New Mexico', 'Texas', 'Louisiana', 'North Carolina', 'North Dakota', 'Nebraska',
    'Tennessee', 'New York', 'Pennsylvania', 'Alaska', 'Nevada', 'Virginia', 'Colorado', 'California', 'Alabama',
    'Arkansas', 'Vermont', 'Illinois', 'Georgia', 'Indiana', 'Iowa', 'Massachusetts', 'Arizona', 'Idaho', 'Maine',
    'Maryland', 'Oklahoma', 'Ohio', 'Utah', 'Missouri', 'Minnesota', 'Michgan', 'Rhode Island', 'Kansas', 'Montana',
    'Mississippi', 'South Carolina', 'Kentucky', 'Oregon', 'South Dakota')


def main():
    print lookup.lookup(check("washington"))


def clean_str(str):
    return re.sub(r"[^a-z]", "", str.lower())


def check(str):
    if len(str) != 2:
        for state in states:
            if clean_str(str) == clean_str(state):
                print str, state
                return state
    else:
        return str


if __name__ == "__main__":
    main()
