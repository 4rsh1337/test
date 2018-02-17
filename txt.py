#! /usr/bin/python
import sys
import os
from termcolor import colored
if os.getuid() != 0:
        print("Are you root? Please execute as root")
        print("try sudo htb")
        exit()
        
print colored('''
                        ____________________________
                       |      ____  _  _       _    |
                       |     |  _ \| || |     | |   |
                       |     | |_) | || |_ _  | |   |
                       |     |  _ <|__   _| |_| |   |
                       |     |_| \_\  |_|  \___/    |
                       |____________________________|
 
''', 'blue')
print colored('''                   HackTheBox Vulnerability Scanner By R4J ''', 'red')
print colored('''             YouTube - https://youttube.com/tutorialsforkalilinux ''', 'red')

print " "
print " "
import urllib
a=urllib.urlopen("http://ipecho.net/plain")
ip=a.read()
print "your public ip address is: ",ip