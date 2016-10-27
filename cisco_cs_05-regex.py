#Program to scan a config file and output objects
#Author:	A. Gittins
#Date:		26/10/16
#Version:	5



from ciscoconfparse import CiscoConfParse

configFileName = raw_input("Please provide the name of the config file in the files folder: ")
objectListFileName = raw_input("Please provide the name of the object list file in the files folder: ")
folderPath = 'C:/Users/agittins/vagrant_image/trusty/python-apps/cisco_config_scraper/cisco_config_scraper/scripts/files/'

configFile = open(folderPath + configFileName + ".txt", 'r')
objectListFile = open(folderPath + objectListFileName + ".txt", 'r') 


configList = [x.rstrip() for x in configFile]
objectList = [x.rstrip() for x in objectListFile]

#print str(configFile.read())
#print str(objectListFile.read())


#working list comprehension
listOfObjectsInBoth = [e for e in objectList if e in configList]

#using endswith method
#listOfObjectsInBoth = [e for e in objectList if e.endswith() in configList]

print str(listOfObjectsInBoth)
print ""
print ""
print ""

# for object in objectList:
#     isIn = " is in config"
#     isNotIn = "is not in config"
#     loopObject = object
#     regexPattern = loopObject + r"$"
#     #print loopObject
#     #print ""
#     for line in configList:
#         #print "Starting lookup for " + loopObject
#         if regexPattern in line:
#             print loopObject
#         #debugging print out

	