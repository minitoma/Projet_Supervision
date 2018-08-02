#!/usr/bin/python
# Created by CALATAYUD Thomas -- 2018
import sys
import os

def switchToSaeir():
    os.rename("/etc/resolv.conf", "/etc/resolv.conf.cg49")
    os.rename("/etc/resolv.conf.saeir", "/etc/resolv.conf")

def switchToCG49():
    os.rename("/etc/resolv.conf", "/etc/resolv.conf.saeir")
    os.rename("/etc/resolv.conf.cg49", "/etc/resolv.conf")

if __name__ ==  "__main__":
    if len(sys.argv) == 2:
        if '--help' ==  sys.argv[1]:
            print("##### This script switch the resolv.conf file to perform to the saeir or cg49 domain #####")
            print
            print("You may need to use this script with sudo")
            print("Usage :")
            print("    --cg49 to switch resolv.conf for the cg49 domain")
            print("    --saeir to switch resolv.conf for the saeir domain")
            print("    --help to show this help")
        elif '--cg49' == sys.argv[1]:
            try:
                if os.path.isfile("/etc/resolv.conf.cg49"):
                    switchToCG49()
                    print("switching /etc/resolv.conf for the cg49 domain")
                else:
                    print("resolv.conf is already configure for the cg49 domain")
            except:
                print("*** WARNING ***")
                print("You have no right to use this script !")
                print("Try to use sudo !")
        elif '--saeir' == sys.argv[1]:
            try:
                if os.path.isfile("/etc/resolv.conf.saeir"):
                    switchToSaeir()
                    print("switching /etc/resolv.conf for the saeir domain")
                else:
                    print("resolv.conf is already configure for the seair domain")
            except:
                print("*** WARNING ***")
                print("You have no right to use this script !")
                print("Try to use sudo !")
        else:
            print("Unknown argument, --help for more help")
    else:
        print("Unknown command or missing arguments, --help for more help")
        sys.exit(2)
        sys.exit(0)
else:
    print("Help with --help" % sys.argv[0])
    sys.exit(2)
