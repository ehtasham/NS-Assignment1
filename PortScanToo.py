import threading
import Queue
import time
import sys
import os
import socket

if (len(sys.argv) !=2) :
	print "enter the name of remoteServer"
	os._exit(0)
remoteServer=str(sys.argv[1])
remoteServerIP  = socket.gethostbyname(remoteServer)
total_ports=1000

def port_scan(port):
	# print "scanning port {} ".format(port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((remoteServerIP, port))
	if result == 0:
		service_name=socket.getservbyport(port)
		
		print('Port: %s Open  Service :  %s  ' % \
			(port,service_name))
	sock.close()
	if(port==total_ports-1):
		t2 = time.time()
		time_difference =  t2 - t1
		scan_rate=total_ports/time_difference
		print ('Scanning Completed in: %s seconds '% time_difference)
		print ('Scan Rate: %s  '% scan_rate)
		os._exit(0)

def threading_module():
    while True:
       	thread = q.get()
        port_scan(thread)

q = Queue.Queue()

t1 = time.time()
for th in range(30):
     thr = threading.Thread(target=threading_module)
     thr.start()

for thread in range(total_ports):
    q.put(thread)
