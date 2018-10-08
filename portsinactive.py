#!/usr/bin/env python

import getpass
import ipaddress
import datetime

days = 0
intlist = []
CurrentDate = datetime.datetime.now()

user = raw_input("Enter your username: ")
password = getpass.getpass()

import ipaddress
def ipEntered():
    while True:
        try:
            val = raw_input("Enter IP address: ")
            return ipaddress.ip_address(bytearray(val))
        except ValueError:
            print ("Invalid")

ipaddress = str(ipEntered())

while True:
    days = raw_input("Enter days of inactive port: ")
    try:
        numchk1 = int(days)
    except ValueError:
        print("Needs to be numeric") 
    else:
        break

from netmiko import ConnectHandler
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': ipaddress,
    'username': user,
    'password': password,
}

net_connect = ConnectHandler(**iosv_l2)
cmd1 = net_connect.send_command('show interface status | inc notconnect')
for line in cmd1.splitlines():
    intlist.append(line.split(" ")[0])

for interface in intlist:
    if "Po" not in interface:
        rawcmd = "show dtp interface " + interface
        cmd2 = net_connect.send_command(rawcmd)
        if not cmd2:
            print interface
        else:
            if "0 link downs" not in cmd2:
                linkdown = cmd2.splitlines()[-1]
                rawlinkdowndate = linkdown.split("down on ")[1]
                linkdowndate = datetime.datetime.strptime(rawlinkdowndate, '%a %b %d %Y, %H:%M:%S')
                daysinactive = int((CurrentDate.date()-linkdowndate.date()).days)
                if daysinactive > numchk1:
                    print interface
            else:
                print interface
