import threading
import Queue
import time
import socket
import sys




remoteServer=str(sys.argv[1])
remoteServerIP  = socket.gethostbyname(remoteServer)


def portscan(port):
	# print "scanning port {} ".format(port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((remoteServerIP, port))
	if result == 0:
		service_name=socket.getservbyport(port)
		print('Port: %s Open  ' % port)
	sock.close()



# The threader thread pulls an thread from the queue and processes it
def threader():
    # while True:
        # gets an thread from the queue
	thread = q.get()

        # Run the example job with the avail thread in queue (thread)
	portscan(thread)

        # completed with the job
	q.task_done()



        

# Create the queue and threader 
q = Queue.Queue()

# how many threads are we going to allow for
for x in range(30):
     t = threading.Thread(target=threader)



     # begins, must come after daemon definition
     t.start()


start = time.time()

# 100 jobs assigned.
for thread in range(1,100):
    q.put(thread)

# wait until the thread terminates.
q.join()