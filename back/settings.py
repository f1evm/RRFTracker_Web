#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFTracker version Web
Learn more about RRF on https://f5nlg.wordpress.com
Check video about RRFTracker on https://www.youtube.com/watch?v=rVW8xczVpEo
73 & 88 de F4HWN Armel
'''

# Version

version = '2.0.4'

# Default room and path

room = 'RRF'            # Room: Default value !
log_path = '/tmp/RRF'   # Log path: Default value !
log_path_day = ''		# Log path day: Default value !

# Set call

call = ['', '', '', '', '', '', '', '', '', '']         # Call list
call_date = ['', '', '', '', '', '', '', '', '', '']    # Call date list
call_time = ['', '', '', '', '', '', '', '', '', '']    # Call time list
call_current = call[0]                                  # Call current
call_previous = call[1]                                 # Call previous

qso = 0                 	# QSO count
qso_hour = [0] * 24     	# QSO list for histogramm
node_count = 0          	# Node count
node_count_max = 0      	# Node count max
node_count_min = 10**4  	# Node count min
user_count = 0              # User count

node_list = []          	# Node list
node_list_old = []      	# Node list
node_list_in = []       	# Node list in
node_list_out = []      	# Node list out

day_duration = 0        	# Total emission time

node = dict()           	# Node dict
porteuse = dict()       	# Porteuse dict

transmit = True         	# Detect transmit
stat_save = False       	# If False, stat need to be save
geolocalisation = {}    	# Geolocalisation

# Set time and date

tot_start = ''
tot_current = ''
hour = ''
minute = ''
seconde = ''
duration = 0
intempestif = 2         # Tuned me !!!
main_loop = .250        # Main loop tempo

# Set init

init = True				# Check if init...

# Set url

# http://rrf2.f5nlg.ovh:8000/status-json.xsl

room_list = {
    'RRF': {
        'url': 'http://rrf.f5nlg.ovh/api/svxlink/RRF',
        'dtmf': '9 6 #'
    },
    'RRF_V1': {
        'url': 'http://rrf.f5nlg.ovh/api/svxlink/RRF V1',
        'dtmf': '9 6 #'
    },
    'TECHNIQUE': {
        'url': 'http://rrf.f5nlg.ovh/api/svxlink/technique',
        'dtmf': '9 8 #'
    },
    'INTERNATIONAL': {
        'url': 'http://rrf.f5nlg.ovh/api/svxlink/international',
        'dtmf': '9 9 #'
    },
    'BAVARDAGE': {
        'url': 'http://rrf.f5nlg.ovh/api/svxlink/bavardage',
        'dtmf': '1 0 0 #'
    },
    'LOCAL': {
        'url': 'http://rrf.f5nlg.ovh/api/svxlink/local',
        'dtmf': '1 0 1 #'
    },
    'FON': {
        'url': 'http://rrf.f5nlg.ovh/api/svxlink/FON',
        'dtmf': '9 7 #'
    }
}
