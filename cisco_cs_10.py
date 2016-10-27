#Program to scan a config file and output objects
#Author:	A. Gittins
#Date:		27/10/16
#Version:	10

import pprint

configFile = open('C:/Users/agittins/vagrant_image/trusty/python-apps/cisco_config_scraper/cisco_config_scraper/scripts/files/dr-e-wan-config.txt')
conf = [x.rstrip() for x in configFile]

objectListFile = open('C:/Users/agittins/vagrant_image/trusty/python-apps/cisco_config_scraper/cisco_config_scraper/scripts/files/pr-o-cp_object-list.txt')
objct = [x.rstrip() for x in objectListFile]


dupObjectList = [o for o in objct for c in conf if c.endswith(o)]
pprint.pprint(sorted(dupObjectList))