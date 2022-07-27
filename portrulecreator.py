# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 17:09:33 2022

@author: space-cola
"""


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
        print ("\nYou have selected " + tcpPorts[20])
    elif selection == "2": 
        print ("\nYou have selected " + tcpPorts[21])
    elif selection == "3": 
        print ("\nYou have selected " + tcpPorts[22])
    elif selection == "4": 
        print ("\nYou have selected " + tcpPorts[23])
    elif selection == "5": 
        print ("\nYou have selected " + tcpPorts[25])
    elif selection == "6": 
        print ("\nYou have selected " + tcpPorts[53])
    elif selection == "7": 
        print ("\nYou have selected " + tcpPorts[80]) 
    elif selection == "8": 
        print ("\nYou have selected " + tcpPorts[88]) 
    
    else:
        print ("\nSorry, the option you entered was not recognised, shutting down... ")
        return

userSelect()

def aclRule():
    global action
    action = input ("Please enter permit or deny: ")
    if action == "permit" or action == "deny":
        print ("\nCreating a " + action + " statement...")
    else:
        print ("Error")
        return
    global hostip # makes the hostip variable global as this is carried to a later function
    hostip = input ("Please enter host IP in x.x.x.x format: ")    
    global destinationip #make the destinationip variable global as this is carried to a later function
    destinationip = input ("Please enter destination IP in x.x.x.x format: ")
        
aclRule()
        

def presentation():
    global aclName
    aclName = input ("Please enter a name for your access list, avoiding spaces: ") # could use an if statement following to check for spaces or unacceptable characters
    print ("Please wait...")
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
    
    print ("\nYour Extended access control entry is:")
    print ("\naccess-list "  +  aclName  +" "+  action + " tcp" + " host " + hostip + " host " + destinationip + " eq " + portPort)
    
presentation()
