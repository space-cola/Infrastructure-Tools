"""
Created on Wed Jul 27 17:09:33 2022 (original)
@author: space-cola
"""

import re #used for regex validation functions


tcpPorts = {20:"FTP Data", 21:"FTP Control", 22:"SSH",
23:"Telnet", 25:"SMTP", 53:"DNS", 80:"HTTP",
88:"Kerberos"} # dictionary of common TCP ports typically used for access control entries


def userSelect(): # user selects an option here
    print ("Welcome, here are your options: \n" + 
    "\n1:" + tcpPorts[20] +
    "\n2:" + tcpPorts[21] +
    "\n3:" + tcpPorts[22] +
    "\n4:" + tcpPorts[23] +
    "\n5:" + tcpPorts[25] +
    "\n6:" + tcpPorts[53] +
    "\n7:" + tcpPorts[80] +
    "\n8:" + tcpPorts[88])
    global selection
    selection = input ("\nPlease select a number from the list: ")     
    if selection == "1":
        print ("\nYou have selected " + tcpPorts[20] + " (Port" + " 20)")
    elif selection == "2": 
        print ("\nYou have selected " + tcpPorts[21] + " (Port" + " 21)")
    elif selection == "3": 
        print ("\nYou have selected " + tcpPorts[22] + " (Port" + " 22)")
    elif selection == "4": 
        print ("\nYou have selected " + tcpPorts[23] + " (Port" + " 23)")
    elif selection == "5": 
        print ("\nYou have selected " + tcpPorts[25] + " (Port" + " 25)")
    elif selection == "6": 
        print ("\nYou have selected " + tcpPorts[53] + " (Port" + " 53)")
    elif selection == "7": 
        print ("\nYou have selected " + tcpPorts[80] + " (Port" + " 80)") 
    elif selection == "8": 
        print ("\nYou have selected " + tcpPorts[88] + " (Port" + " 88)") 
    
    else:
        print ("\nSorry, the option you entered was not recognised, shutting down to save processor power... ")
        exit(0)

userSelect()

def aclRule():
    global action
    print ("\nChoose permission action")
    while True:
        action = input ("Please enter 'permit' or 'deny': ")
        if action == "permit" or action == "deny":
            print ("\nCreating a " + action + " statement...")
            break
        else:
            print ("Error, please re-enter")

aclRule()

def sourceValidation(): #validates source ip using regex
    global sourceip          
    while True:
        sourceip = input ("\nNow enter the Source IP in x.x.x.x format: ")
        sourceipMatch = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", sourceip) #checks for dotted decimal x.x.x.x format
        if (bool(sourceipMatch)) == True: #if format matches
            print ("\nProcessing...")
            break
        else:
            print ("Error, please re-enter")

sourceValidation()

def destinationValidation(): #validates destination ip using regex
    global destinationip          
    while True:
        destinationip = input ("\nNow enter the Destination IP in x.x.x.x format: ")
        destinationipMatch = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", destinationip) #checks for dotted decimal x.x.x.x format
        if (bool(destinationipMatch)) == True: #if format matches
            print ("\nProcessing...")
            print ()
            break
        else:
            print ("Error, please re-enter")

destinationValidation()


def nameValidation(): #validates ACL name using regex
    global aclName
    while True:
        aclName = input ("Please enter a name for the access list, avoiding spaces:")
        aclNameMatch = re.match(r"^(.*\s+.*)+$", aclName) #checks string for whitespace
        if (bool(aclNameMatch)) == False: #if no whitespace
            print ("Please wait...")
            break
        else:
            print ("\nError! Whitespace detected, Please re-enter")

nameValidation()    
    
def presentation():   
    if selection == "1":
        portPort = "20"
    elif selection == "2": 
        portPort = "21"
    elif selection == "3": 
        portPort = "22"
    elif selection == "4": 
        portPort = "23"
    elif selection == "5": 
        portPort = "25"
    elif selection == "6": 
        portPort = "53"
    elif selection == "7": 
        portPort = "80"
    elif selection == "8": 
        portPort = "88"
    
    print ("\nYour extended access control entry is:")
    print ("\naccess-list "  +  aclName  +" "+  action + " tcp" + " host " + sourceip + " host " + destinationip + " eq " + portPort)
    
presentation()
