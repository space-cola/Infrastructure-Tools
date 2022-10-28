# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:19:04 2022

@author: space-cola
"""
from datetime import datetime
import base64


def getCredentials():
    global uName
    uName = input("Enter username: ")
    uPass = input ("Enter password: ")
    #if statement here to validate credentials, or break script
    # Mobile device side - would rely on loginTime variable push 
    global loginTime
    loginTime = datetime.now()
    global token
    token = (uName + str(loginTime)) #creates a string to store username and datetime
    
    
getCredentials()
    
def encoding():
    global encodedToken
    encodedToken = base64.b64encode(token.encode('ascii'))
    global oSecret
    oSecret = 't0pSecret' #organisational secret that regularly changes
    global encodedOSecret
    encodedOSecret = base64.b64encode(oSecret.encode('ascii'))
    global authentication
    
encoding()

def authenticationMatrix():
    longStr = (encodedOSecret + encodedToken)
    hexStr = base64.b64decode(longStr.decode('ascii')).hex() #converts the longStr to hex
    oneTime = hexStr [0:8] #stores first 8 characters, this SHOULD be generated mobile device side

authenticationMatrix()
    

# Next part is authentication of oneTime variable against what the user enters from
# concurrent generation on their mobile device. 