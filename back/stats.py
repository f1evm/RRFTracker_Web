#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFTracker version Web
Learn more about RRF on https://f5nlg.wordpress.com
Check video about RRFTracker on https://www.youtube.com/watch?v=rVW8xczVpEo
73 & 88 de F4HWN Armel
'''

import os
import glob
import datetime
import time
import sys
import getopt


# Ansi color
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Usage
def usage():
    print 'Usage: RRFTracker.py [options ...]'
    print
    print '--help               this help'
    print
    print 'Search settings:'
    print '  --path         set path to RRF files (default=/var/www/RRFTracker/)'
    print '  --pattern      set search pattern (default=current month)'
    print
    print '88 & 73 from F4HWN Armel'

# Convert second to time
def convert_second_to_time(time):
    hours = time // 3600
    time = time - (hours * 3600)

    minutes = time // 60
    seconds = time - (minutes * 60)

    if hours == 0:
        return str('{:0>2d}'.format(int(minutes))) + ':' + str('{:0>2d}'.format(int(seconds)))
    else:
        return str('{:0>2d}'.format(int(hours))) + ':' + str('{:0>2d}'.format(int(minutes))) + ':' + str('{:0>2d}'.format(int(seconds)))


# Convert time to second
def convert_time_to_second(time):
    if len(time) > 5:
        format = [3600, 60, 1]
    else:
        format = [60, 1]

    return sum([a * b for a, b in zip(format, map(int, time.split(':')))])

def main(argv):

    room_list = {
        'RRF',
        'TECHNIQUE',
        'INTERNATIONAL',
        'BAVARDAGE',
        'LOCAL',
        'FON'
    }

    tmp = datetime.datetime.now()

    search_path = '/var/www/RRFTracker/'
    search_pattern = tmp.strftime('%Y-%m')

    # Check and get arguments
    try:
        options, remainder = getopt.getopt(argv, '', ['help', 'path=', 'pattern='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in options:
        if opt == '--help':
            usage()
            sys.exit()
        elif opt in ('--path'):
            search_path = arg
        elif opt in ('--pattern'):
            search_pattern = arg

    print color.BLUE + 'Path ' + color.END + search_path,
    print ' with ',
    print color.BLUE + 'Pattern ' + color.END + search_pattern,
    print '...'

    time_super_total = 0

    for r in room_list:

        print color.BLUE + r + color.END
        path = search_path + r + '-' + search_pattern + '-*/abstract.json'
        file = glob.glob(path)
        file.sort()

        time_total = 0

        for f in file:
            if os.path.isfile(f):
                with open(f, 'r') as content_file:
                    content = content_file.read()

                    # Indicatif

                    search_start = content.find('Emission cumulée": "') # Search this pattern
                    search_start += 21                                  # Shift...
                    search_stop = content.find('"', search_start)       # And close it...

                    print f, '-->', content[search_start:search_stop]

                    time_total += convert_time_to_second(content[search_start:search_stop])
        time_super_total += time_total
        print 'Total:', convert_second_to_time(time_total)
    print 'Total cumulée:', convert_second_to_time(time_super_total)

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
