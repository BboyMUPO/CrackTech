#I DON'T GET THE RISK FOR ANYTHING
import socket
import os
import appuifw

def crack(wifi):
    your_list = 'qwertzuiopasdfghjklíyxcvbnm' #latters you want to use in brute-force attack
    complete_list = []
    for current in xrange(2): #how long the password is default 2
        a = [i for i in your_list]
        for y in xrange(current):
            a = [x+i for i in your_list for x in a]
        complete_list = complete_list+a #Yeah it's the brute force

def connect():
    apid = socket.select_acces_point() #On some deviece wlantools.scan() freeze and it's faster too.please select a wifi hotspot not an internet connection.
    apo = socket.acces_point(apid)
    apo.start

crack(connect())
