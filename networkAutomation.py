# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 17:26:14 2022

@author: Lenovo P50
"""


from ipaddress import IPv4Network
subnetA = IPv4Network('192.168.0.0/24')
subnetA.num_addresses
subnetDict = {}

availHosts = subnetA.hosts()

def autoAddress():
    for addr in subnetA:
        str(subnetA.IPv4Network)
autoAddress()

def autoAssign():
    for x in range (0,253):
        globals()['host%s' % x] = 'placeholder'
        
autoAssign()


for ip in availHosts:
    subnetDict = {}
    
ipaddress = []
    

for h in subnetA.hosts():
    java = print(subnetA.hosts)
    ipaddress.append(hosts)


h = subnetA.hosts()
# type(h)
next(h)
# next(h)


for n in range(0, 7):
    globals()['strg%s' % n] = 'Hello'
# strg0 = 'Hello', strg1 = 'Hello' ... strg6 = 'Hello'

for x in range(0, 7):
    globals()[f"variable1{x}"] = f"Hello the variable number {x}!"