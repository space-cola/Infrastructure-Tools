# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:35:32 2022

@author: Martin Boa
"""

import ipaddress #import IP address library for IP decimal conversion
import random #use to pick an IP from decimal range

privateAddresses = {"A": "10.0.0.0", "B": "172.16.0.0", "C": "192.168.0.0"} #dictionary to store IP addresses


def networkRetrieval():
    global department #declare department variable as global
    department = input ("Enter the department name: ")
    if department == "management":
        print ("\nThe reserved network address space for " + department + " is " + privateAddresses  ["A"])
    elif department == "sales":
        print ("\nThe reserved network address space for " + department + " is " + privateAddresses  ["B"])
    elif department == "human resources":
        print ("\nThe reserved network address space for " + department + " is " + privateAddresses ["C"])
    else:
        print ("\nDepartment not recognised")
        return
    
networkRetrieval()

if department == "management" or department == "sales" or department == "human resources": # evaluates contents of department variable
    print ("\nThe following is a random assignable IP address from this department: ")
else: 
    print ("\nError! ") #if no matches, ERROR!
    
def randSubnetIP(): 
    if department == "management": # uses random to pick a number between the decimal ranges of an IP subnet
        randomAddress = (random.randint(167772161, 184549374)) #excludes 10.0.0.0 and 10.255.255.255
        print(ipaddress.ip_address(randomAddress)) #prints the conversion of the random decimal back to an IP address
   
    
    elif department == "sales":
        randomAddress = (random.randint(2886729729, 2887778302)) #excludes 172.16.0.1 and 172.31.255.255
        print(ipaddress.ip_address(randomAddress))
        
    elif department == "human resources":
        randomAddress = (random.randint(3232235521, 3232301054)) #excldues 192.168.0.0 and 192.168.255.255
        print(ipaddress.ip_address(randomAddress))
        
    else:
        print ("\nCouldn't locate an IP address, please retry") # prints if the conditions of networkRetrieval aren't met
        return
        
randSubnetIP()

