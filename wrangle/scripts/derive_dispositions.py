import argparse
from loggy import loggy
from pathlib import Path
import re
from sys import stdout
import yaml

LOGGY = loggy('derive_dispositions')
A_CROSSWALK = yaml.load(Path('wrangle', 'scripts', 'etc', 'additional-dispositions-map.yaml').read_text())
P_CROSSWALK = yaml.load(Path('wrangle', 'scripts', 'etc', 'person-map.yaml').read_text())


# Possible values:

# "AR, AM2TAS, P"
# OF2TCN
# "OM3IWN, WM3IWN, WF2IWN, WM2IWN, BM2IAS, P"
# "HM3TWN, HM3TCN"
# "HM3TWN, zz do not use Assist"
# AR
# M


def derive_disposition(rawtxt):
    """
    rawtxt: str; the raw value from input, could be "OF2TCN" or "AR, AM2TAS, P"
    Returns: dict;
    """
    return [_map_disposition(val) for val in _split_dispositions_text(rawtxt)]



def _split_dispositions_text(rawtxt):
    """
    rawtxt: str; the raw value from input, could be "OF2TCN" or "AR, AM2TAS, P"
    Returns: list; "AR, AM2TAS" becomes ["AR", AM2TAS]
    """
    return re.split(r' *, *', rawtxt.strip().replace('"', ''))

def _map_disposition(valuetxt):
    """
    Returns: tuple(string, dict);
    for "BM4IWN":
        ('person', 'race': 'black', 'gender': 'M',
                 'age_range': 40_and_over, 'reason': 'investigation',
                 'enforcement': 'warning', 'car_searched': 'N')
    """

    # check to see if this value refers to a person
    # quick heuristic is if it is six chars and the
    # first letter refers to a race, second to gender
    response = {'warnings': [], 'original': valuetxt}
    if len(valuetxt) == 6 and valuetxt[0] in P_CROSSWALK[0]['enums'].keys() \
        and valuetxt[1] in P_CROSSWALK[1]['enums'].keys():
        response['type'] = 'person'
        response['data'] = {}
        for i, k in enumerate(valuetxt):
            attr = P_CROSSWALK[i]['name']
            emap = P_CROSSWALK[i]['enums']
            if not emap.get(k):
                w = '%s does not have key %s' % (attr, k)
                d['warnings'].append(w)
                LOGGY.warn(w)
                response['data'][attr] = k
            else:
                response['data'][attr] = emap[k]['value']

    elif valuetxt == '':
        LOGGY.warn("Blank value")
        response['warnings'].append("Blank value")
        response['type'] = 'blank'
    else:
        response['type'] = 'additional_disposition'
        if not A_CROSSWALK.get(valuetxt):
            w = 'Non-existent key for %s' % valuetxt
            LOGGY.warn(w)
            response['warnings'].append(w)
        else:
            response['data'] = A_CROSSWALK[valuetxt]['value']

    return response



if __name__ == '__main__':
    """
    Passing in raw input without logic to attach to the rest of the row
    only needs to be done for debugging purposes
    """

    parser = argparse.ArgumentParser("Parse dispositions column")
    parser.add_argument('infile', type=argparse.FileType('r'), help="Filename or stdin containing one column text stream")
    args = parser.parse_args()

    infile = args.infile
    LOGGY.info("Reading from %s" % infile.name)

    for line in infile:
        for d in derive_disposition(line):
            stdout.write(str(d) + "\n")



