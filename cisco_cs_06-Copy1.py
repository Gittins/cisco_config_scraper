#Program to scan a config file and output objects
#Author:	A. Gittins
#Date:		26/10/16
#Version:	4



from ciscoconfparse import CiscoConfParse

#configFileName = raw_input("Please provide the name of the config file in the files folder: ")
#objectListFileName = raw_input("Please provide the name of the object list file in the files folder: ")
folderPath = '/vagrant/python-apps/cisco_config_scraper/cisco_config_scraper/scripts/files/'

#configFile = open(folderPath + configFileName + ".txt", 'r')
#objectListFile = open(folderPath + objectListFileName + ".txt", 'r') 

configFile = open('/vagrant/python-apps/cisco_config_scraper/cisco_config_scraper/scripts/files/config.txt')
objectListFile = open('/vagrant/python-apps/cisco_config_scraper/cisco_config_scraper/scripts/files/object-list.txt')

print str(configFile.read())
print str(objectListFile.read())

DMIN = ["DM_INLINE_NETWORK_1", "DM_INLINE_NETWORK_2"]

tester = [e for e in DMIN if e in configFile]
print tester

#for object in objectListFile:
#    isIn = " is in config"
#    isNotIn = "is not in config"
#    loopObject = object
#    print loopObject
#    #print ""
#    for line in configFile:
#        print "Starting lookup for " + loopObject
#        if loopObject in line:
#            print object
        #debugging print out


#for item in list:
#    if conditional:
#        expression