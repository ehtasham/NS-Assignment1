import threading
import Queue
import time
import sys
import os
import socket

remoteServer=str(sys.argv[1])
remoteServerIP  = socket.gethostbyname(remoteServer)
total_ports=1000

def port_scan(port):
	print "scanning port {} ".format(port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((remoteServerIP, port))
	if result == 0:
		service_name=socket.getservbyport(port)
		print('Port: %s Open  ' % port)
	sock.close()
	if(port==999):
		os._exit(0)

def threading_module():
    while True:
       	thread = q.get()
        port_scan(thread)

q = Queue.Queue()

for th in range(30):
     thr = threading.Thread(target=threading_module)
     thr.start()

for thread in range(1000):
    q.put(thread)
