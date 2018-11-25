# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:33:39 2018
Provide statistics on files containing xml MARC/ISO2709 records (an adaptation to a script originally designed by Ed Summers)
@author: hagay


"""

import pymarc
import sys
import time

# Return the MARC records as an array
def get_records(marc_file):
    if marc_file.lower().endswith(('.xml')):
        print ('xml')
        records = pymarc.parse_xml_to_array(marc_file)
    elif marc_file.lower().endswith(('.mrc')):
        print ('mrc')
        records = pymarc.MARCReader(open(marc_file, "rb"))    
    return records

# assuming 'b' is 100%, what is the precntage value of 'a'  
def percentage_of(a,b):
    return (a * 100) / b

def create_stats(filename):
    stats = {}
    records = 0
    for record in get_records(filename):
        records +=1
        for field in record.fields:
            stats[field.tag] = stats.get(field.tag, 0) + 1
    stats['rec_count'] = records
    return stats

def collect_stats(files):
    full_stats = {}
    for filename in files:
        full_stats[filename] = create_stats(filename)
    return full_stats
  
def main():
    files = [filename for filename in sys.argv[1:]]
    stats = collect_stats(files)
    #print (stats)
    report_file_name = "report" + time.strftime("%Y%m%d-%H%M%S") + '.txt'
    for file in stats:
        rec_count = stats[file]['rec_count']
        stats[file].pop('rec_count', None)
        f = open(report_file_name, "a")
        f.write("\nStats for file: {0} (includes {1} records)\n\n".format(file,rec_count))
        print ("\nStats for file: {0} (includes {1} records)\n\n".format(file,rec_count))
        for value in (stats[file]):
            f.write("Field No. {0} : {1} results, ({2:.2f}) %\n".format(value, stats[file][value], percentage_of(stats[file][value], rec_count)))
            print ("Field No. {0} : {1} results, ({2:.2f} %)".format(value, stats[file][value], percentage_of(stats[file][value], rec_count)))
    print ('the report is saved in file: {0}'.format(report_file_name))

main()
