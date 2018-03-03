#!/usr/bin/env python
import socket
import sys
from datetime import datetime

remoteServer=str(sys.argv[1])
remoteServerIP  = socket.gethostbyname(remoteServer)


# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors
for port in range(1,17):  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
        print "Port {}: 	 Open".format(port)
    sock.close()


# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total