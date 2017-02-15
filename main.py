# -*- coding: utf-8 -*-

import sys
import urllib
import subprocess
import argparse

# Constants
URL = "http://www.gifu-nct.ac.jp/gakka/keijiyou/keijiyou.pdf"
LOCALPDF = "keijiyou.pdf"
LOCALTEXT = "keijiyou.txt"

def download():
    urllib.urlretrieve(URL, LOCALPDF)

def pre_parse():
    cmd = "pdftotext -raw " + LOCALPDF + " " + LOCALTEXT 
    #print("done:" + cmd)
    let = subprocess.check_call( cmd.split(" ") )
    return let

def filter1(gakunen, gakka, map):
    return filter(lambda item:item['gakka'] is gakka and item['gakunen'] is gakunen, map) 

def filter2(gakunen, map):
    return filter(lambda item:item['gakunen'] is gakunen, map) 

def parse():
    """
    map ver2.0
    map = [{
            date: '',
            weeks: '',
            jigen: '',
            gakka: '',
            gakunen: '',
            old:[{
                teacher: '',
                subject: '',
            }],
            new:[{
                teacher: '',
                subject: '',
            }]
        }]
    """
    """
    map = [{
            date: '',
            weeks: '',
            jigen: '',
            gakka: '',
            gakunen: '',
            data: '',
        }]
    """
    map = []

    for line in open(LOCALTEXT, "r"):
        terms = line.split(" ")
        # discard headers
        # change conditions if need
        if line.find("教員名") is not -1 or len(terms) < 5 or line is "":
            continue
        # read body
        map.append({
            'date': terms[0],
            'weeks': terms[1],
            'jigen': terms[2],
            'gakka': terms[3],
            'gakunen': terms[4],
            'data': str([terms[i] for i in range(5, len(terms))])
        })

    return map


if __name__ == "__main__":
    # arg check
    parser = argparse.ArgumentParser()
    parser.add_argument('--cache',help='Using cache, not download original pdf')
    parser.add_argument('--filter',help='[1E|2E|2C etc...]')
    args = parser.parse_args()
    
    # execute
    if args.cache is not None:
        download()
    pre_parse()
    data = parse()
    
    # use filter
    if args.filter is not None:
        data = filter1(args.filter[0], args.filter[1], data)
    
    if len(data) is 0:
        print "No data."
    
    for item in data:
        print item['date'] + item['weeks']

    
    #data = filter2('3', data)
    #print data[0]['date']
    
    #print str(data)
    




