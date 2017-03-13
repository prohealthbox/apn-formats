import re
from fuzzywuzzy import fuzz
from apn import APNS

states = (
    'Washington', 'Delaware', 'District of Columbia', 'Wisconsin', 'West Virginia', 'Hawaii', 'Florida', 'Wyoming',
    'New Hampshire', 'New Jersey', 'New Mexico', 'Texas', 'Louisiana', 'North Carolina', 'North Dakota', 'Nebraska',
    'Tennessee', 'New York', 'Pennsylvania', 'Alaska', 'Nevada', 'Virginia', 'Colorado', 'California', 'Alabama',
    'Arkansas', 'Vermont', 'Illinois', 'Georgia', 'Indiana', 'Iowa', 'Massachusetts', 'Arizona', 'Idaho', 'Maine',
    'Maryland', 'Oklahoma', 'Ohio', 'Utah', 'Missouri', 'Minnesota', 'Michigan', 'Rhode Island', 'Kansas', 'Montana',
    'Mississippi', 'South Carolina', 'Kentucky', 'Oregon', 'South Dakota')


def clean_str(str):
    return re.sub(r"[^a-z]", "", str.lower())


def verify_state(str):
    max = 79
    name = ""
    for state in states:
        ratio = fuzz.ratio(clean_str(str), clean_str(state))
        if ratio > max:
            max = ratio
            name = state
    if max > 79:
        print name, max
        return name
    else:
        raise Exception("Lookup Error: State name is not recognized.")


def verify_county(str, county):
    ratio = fuzz.ratio(clean_str(str), clean_str(county))
    if ratio > 79:
        return ratio
    else:
        return 0


def lookup(state=None, county=None):
    if county and state is None:
        raise Exception("Lookup Error: Need to specify what state the county resides in.")
    else:
        if state:
            if len(state) != 2:
                state = verify_state(state)
            else:
                pass
            if county:
                results = {state: {county: []}}
                max = 0
                county_name = ""
                formats = []
                for obj in APNS:
                    if obj.state == state or state == obj.state_abbrev:
                        if county_name == obj.county:
                            formats.append(obj.apn_format)
                        else:
                            ratio = verify_county(county, obj.county)
                            if ratio > 0:
                                if ratio > max:
                                    max = ratio
                                    county_name = obj.county
                                    formats = [obj.apn_format]
                                else:
                                    pass
                            else:
                                pass
                    else:
                        pass
                if county_name != "":
                    results = {state: {county_name: formats}}
                else:
                    raise Exception("Lookup Error: County name is not recognized.")
            else:
                results = {state: {}}
                for obj in APNS:
                    if obj.state == state or obj.state_abbrev == state:
                        if obj.county in results[state]:
                            results[state][obj.county].append(obj.apn_format)
                        else:
                            results[state][obj.county] = [obj.apn_format]
                    else:
                        pass
        else:
            results = {}
            for obj in APNS:
                if obj.state in results:
                    if obj.county in results[obj.state]:
                        results[obj.state][obj.county].append(obj.apn_format)
                    else:
                        results[obj.state][obj.county] = [obj.apn_format]
                else:
                    results[obj.state] = {obj.county: [obj.apn_format]}
        return results
