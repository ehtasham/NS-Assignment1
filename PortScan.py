#!/usr/bin/env python
import socket
import sys
from datetime import datetime
import time


total_ports=23
if (len(sys.argv) !=2) :
	print "enter the name of remoteServer"
	exit()
remoteServer=str(sys.argv[1])
remoteServerIP  = socket.gethostbyname(remoteServer)

t1 = time.time()
for port in range(1,23): 
	print "scanning port {} ".format(port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((remoteServerIP, port))
	if result == 0:
		service_name=socket.getservbyport(port)
		print('Port: %s Open  Service :  %s  ' % \
			(port,service_name))
	sock.close()

t2 = time.time()
time_difference =  t2 - t1
scan_rate=total_ports/time_difference

print ('Scanning Completed in: %s seconds '% time_difference)
print ('Scan Rate: %s  '% scan_rate)