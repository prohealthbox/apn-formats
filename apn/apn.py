import pickle
import re

import jellyfish
from pkg_resources import resource_stream

APNS = []
ABBR_RE = re.compile(r'^[a-zA-Z]{2}$')


class Apn(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        return "<APN:%s>" % self.apn_format

    def __str__(self):
        return self.apn_format


def load_apns():
    with resource_stream(__name__, 'apns.pkl') as pklfile:
        for s in pickle.load(pklfile):
            apn = Apn(**s)
            APNS.append(apn)


def lookup(state=None, county=None):

    if state is None:
        if ABBR_RE.match(state):
            state = state.upper()
            state_field = 'state_abbrev'
        else:
            state = jellyfish.metaphone(unicode(state, encoding='utf-8'))
            state_field = 'state_name_metaphone'
    elif state is not None:
        state_field = 'state'

    if county is None:
        county = jellyfish.metaphone(unicode(county, encoding='utf-8'))
        county_field = 'county_name_metaphone'

    elif county is not None:
        county_field = 'county'

    to_return = []
    for apn in APNS:
        if state == getattr(apn, state_field) and county == getattr(apn, county_field):
            to_return.append(apn)
    return to_return


load_apns()
