# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:03:22 2022

@author: space-cola
"""

import random
from sys import exit

storedSecrets = {"Entries":[]} #dictionary object to hold username:secret pairs

def userEntry():
    global confUName # this variable contains the verfied username 
    uName = input('Please enter a username:\n')
    vuName = input ('Please confirm your username:\n')
    if vuName != uName: #if the username's don't match, the programme doesn't run
        print ("Sorry, usernames don't match")
        exit()
    else:
        confUName = vuName
    # code potentially here to compare entered username to usernames already existing on the database
    
userEntry()


def tokenGenerator():
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@%&*()^.,?><!-_+=~`' #alphanumeric alphabet
    number = 10 #10 tokens
    length = 10 #10 characters length
    global tokens
    tokens = []
    for n in range(number):
        token = ""
        for c in range(length): #
            token += random.choice(chars) #10 random tokens generated, 10 characters long using random library
        tokens.append(token) #tokens generated are appended to global tokens list variable
    randToken = random.choice(tokens) #a random one of the 10 tokens is selected
    global secretToken
    secretToken = confUName + ":" + randToken #username:token pair created
    storedSecrets["Entries"].append(secretToken) #username:token appended to dictionary

tokenGenerator()

#this is just for console feedback to confirm it works, in practice this feedback would be hidden
print ("\nPrinting For Demo Purposes only:")
print ("token:pair = "+ secretToken)
