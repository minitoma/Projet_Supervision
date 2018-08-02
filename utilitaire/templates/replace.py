#!/usr/bin/python
# Created by CALATAYUD Thomas -- 2018
import sys
import xml.etree.ElementTree as ET

def searchTag(tag,fileToOpen,message):
    try:
        tree = ET.parse(fileToOpen)
        root = tree.getroot()
        print(tree)
        print(root)
        for tag in root.iter(tag):
            tag.text = str(message)
            print(tag.text)
        tree.write(fileToOpen)
    except:
        print("** ERROR !!! **")
        print(fileToOpen+" is not a valid xml file")

if __name__ ==  "__main__":
    if len(sys.argv) == 2:
        if '--help' ==  sys.argv[1]:
            print("##### This script is using to replace a text from a specific tag in a xml file #####")
            print
            print("Usage (arguments must be in this order):")
            print("    -f <xml file to modify>")
            print("    -t <tag to search> ; for exemple : trends or history")
            print("    -r <text to replace> ; this text would be between the tag you search with the -t argument")
    elif len(sys.argv) == 7:
        if '-f' == sys.argv[1] and \
           '-t' == sys.argv[3] and \
           '-r' == sys.argv[5]:
                fileToOpen = sys.argv[2]
                tag = sys.argv[4]
                message = sys.argv[6]
                searchTag(tag,fileToOpen,message)
        else:
            print("Arguments are not in the right order, --help for more help")
    else:
        print("Unknown command or missing arguments, --help for more help")
        sys.exit(2)
        sys.exit(0)
else:
    print("Help with --help" % sys.argv[0])
    sys.exit(2)
