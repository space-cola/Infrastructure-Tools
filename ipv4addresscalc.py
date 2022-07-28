# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:12:04 2022

@author: space-cola
"""

import ipaddress #use of ipaddress library to create ipaddress objects


userentry = input ("Please enter IP address and mask in x.x.x.x/xx format eg,  1.1.1.1/24: ")
ipGrabber = ipaddress.IPv4Interface(userentry) # converts the address/mask into an ipaddress object
hostIPN = ipGrabber.network # extract the network address parameter from the IPV4
print ("\nInput Information:")

ipInfo = ipGrabber.with_netmask.split('/') #splits the ipaddress and mask into a list
print ("\nIP Address: " + ipInfo[0]) # print only the IP address from the split
maskInfo = userentry.split('/') #perform a split on the user input as this is where the bits in decimal will be entered
print ("Mask bits: " + maskInfo[1]) #print only the bits from the split

print ("\nResults:\n")


# network address
networkAddress = hostIPN.compressed.split('/') #same idea as before, splitting the IP from the mask
print ("Network Address: " + networkAddress[0])

# declaring the hosts in variables early, as they can be used for two purposes
all_hosts = list(hostIPN.hosts()) #use the hosts function normally to iterate all useable hosts, here have sliced the first value in the iteration
firstHost, lastHost = all_hosts[0], all_hosts[-1] #credit to Lyle for solving the overhead problem here with using /8

# broadcast ID
broadcastID = lastHost+1 # can increment lastHost variable by 1 to get broadcast address
broadcast = broadcastID.compressed # converts the previous value into a string so it can be concatenated 
print ("Broadcast ID: " + broadcast)

# wildcard mask
wildcardMask  = hostIPN.with_hostmask #hostmask parameter contains wildcard mask
splitWildcard = wildcardMask.split('/') #split to extract the host address from the wildcard
print ("Wildcard Mask: "+ splitWildcard[-1]) #print the wildcard mask only


# total hosts
totalHosts = hostIPN.num_addresses - 2 # subtract the network and broadcast address from the count
stringTotalhosts = str(totalHosts) #converts to a string so it can be concatenated
print ("Host Addresses: " + stringTotalhosts)
 
#host address range
first = firstHost.compressed #captures the first host string and places in an object
last = lastHost.compressed #extracts the last host string and places in an object
print ("Host Addressable Range: " + first + " to " + last) # prints the available addressable range




