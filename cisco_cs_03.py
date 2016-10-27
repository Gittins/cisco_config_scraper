#Program to scan a config file and output objects
#Author:	A. Gittins
#Date:		26/10/16
#Version:	3



from ciscoconfparse import CiscoConfParse

configFileName = raw_input("Please provide the name of the config file in the files folder: ")
objectListFileName = raw_input("Please provide the name of the object list file in the files folder: ")
folderPath = '/vagrant/python-apps/cisco_config_scraper/cisco_config_scraper/scripts/files/'

configFile = open(folderPath + configFileName + ".txt", 'r')
objectListFile = open(folderPath + objectListFileName + ".txt", 'r') 

#print str(configFile.read())
#print str(objectListFile.read())

def lookupDef(objct2lookup):
    for line in configFile:
        print "Starting lookup for " + objct2lookup
        if objct2lookup in line:
            return str(objct2lookup + isIn)
    return False

	
	
for object in objectListFile:
    isIn = " is in config"
    isNotIn = "is not in config"
    loopObject = object
    print loopObject
	lookupDef(loopObject)
    #print ""
    




print str(lookupDef())