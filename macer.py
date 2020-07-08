#!/usr/bin/python

import os
import re
import optparse
import subproces

def linuxMacChanger(interface, newMac):

    print("[+] changing " + interface + " mac address")
    
    FNULL = open(os.devnull, "w")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", newMac], stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def checkMacChangingProcess(interface, newMac):
    
    if interface == "lo":
        print("you can not change lo Mac Address")
    else:
        interfaceOption = subprocess.check_output(["ifconfig", interface])
        interfaceMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interfaceOption)

        if interfaceMac.group(0) == newMac:
            print("Well done")
        else:
            print("there is a problem")


def showInterfaces():

    #list the network interfaces
    netList = os.listdir('/sys/class/net')

    #list the network interfaces mac address
    macList = []
    counter = 0
    while counter < len(netList):
        interfaceOption = subprocess.check_output(["ifconfig", netList[counter]])
        interfaceMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", interfaceOption)
        if interfaceMac:
            macList.append(interfaceMac.group(0))
        else:
            macList.append("No Mac Address submitted!")
        
        counter += 1
    
    print("Macer")
    print("------------------")
    print("List of network interfaces:")
    print("\n")

    counter = 0
    while counter < len(netList):
        print(" " + netList[counter] +  "      " +  macList[counter])
        counter += 1

    print("\n")
    print("------------------")
    print("by Mahziar Eghdami")

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="choose what interface to change")
parser.add_option("-m", "--mac", dest="newMac", help="the new mac address")
(options, arguments) = parser.parse_args()

if options.interface is None and options.newMac is None:
    showInterfaces()

elif options.interface is None and options.newMac is not None:
    print("[-] you forgot to choose the network interface")

elif options.interface is not None and options.newMac is None:
    print("[-] you forgot to enter a new Mac Address")
    
else:
    interface = options.interface
    newMac = options.newMac
    linuxMacChanger(interface, newMac)
    checkMacChangingProcess(interface, newMac)
