"""
Renames columns, standardizes data
"""

import argparse
from csv import DictWriter, DictReader
from datetime import datetime
from loggy import loggy
from sys import stdout

PACIFIC_TZ_SUFFIX = '-0700'

RAW_HEADERS = ["Incident Number","Call Date/Time", "Location",
                "Incident Type","Dispositions",]

CLEAN_HEADERS = ['incident_number', 'datetime', 'location',
                 'incident_type', 'dispositions',]

LOGGY = loggy("clean_data")

def clean_row(r):
    """Returns a new dict with clean headers and values"""
    d = {}
    d['incident_number'] = r['Incident Number'].strip()
    dt = datetime.strptime(r['Call Date/Time'], '%m/%d/%Y %I:%M:%S %p')
    d['datetime'] =  dt.strftime('%Y-%m-%d %H:%M:%S') + PACIFIC_TZ_SUFFIX
    d['location'] = r['Location'].strip()
    d['incident_type'] = r['Incident Type'].strip()
    d['dispositions'] = r['Dispositions'].strip()
    return d



if __name__ == '__main__':
    parser = argparse.ArgumentParser("Lightly edit the raw Berkeley PD stop data")
    parser.add_argument('infile', type=argparse.FileType('r'), help="Filename or stdin. For the latter, headers won't be echoed to stdout")
    args = parser.parse_args()

    infile = args.infile
    LOGGY.info("Reading from %s" % infile.name)
    csvin = DictReader(infile, fieldnames=RAW_HEADERS)

    csvout = DictWriter(stdout, fieldnames=CLEAN_HEADERS)
    csvout.writeheader()

    for row in csvin:
        if all(h in row.values() for h in ['Incident Number', 'Call Date/Time']):
            pass
        else:
            csvout.writerow(clean_row(row))


