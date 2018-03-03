#!/usr/bin/env python
import dpkt
import datetime
import socket
import pcap
import commands
import time
from dpkt.compat import compat_ord

def inet_to_str(inet):
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)

def print_packets(pcap):
    port_count=0
    previous_port=0
    current_port=0
    check_port=0
    pcap.setfilter("tcp")
    time_difference=0
    # print "t1: ",t1
    for timestamp, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)

        if not isinstance(eth.data, dpkt.ip.IP):
            # print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
            continue

        my_ip=commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]
        ip = eth.data
        src_ip=inet_to_str(ip.src)
        dest_ip=inet_to_str(ip.dst)
        payload=ip.data
        src_port=payload.sport
        dest_port=payload.dport
        current_port=dest_port
        
        if(src_ip == my_ip or dest_ip ==my_ip):
            if(src_ip == my_ip  ):
                # print "outgoing packet"
                if (dest_port==1):
                    t1 = time.time()
                    print "first port"
                    previous_port=current_port
                else:
                    if(current_port != previous_port):
                        check_port=previous_port+1
                        if(current_port!=check_port):
                            print "Not scanning"
                            port_count=0
                            previous_port=current_port
                            t1=time.time()
                            print "t1: ",t1
                        else:
                            t2 = time.time()
                            time_difference=  t2 - t1
                            port_count+=1
                            print "scanning"
                            print "port count: ",port_count
                            previous_port=current_port
                            print "time_difference",time_difference
                            if(port_count > 15 and int(time_difference) >= 5):
                                print "scanner detetected at %s IP", src_ip
            # elif(dest_ip == my_ip):
            #     # print "incoming packet"
        else:
            continue
            # print "not my packet"
        # print('IP Src: %s src port: %s \n IP Dst:  %s  dest port: %s  \n' % \
        #       (src_ip,src_port, dest_ip,dest_port))




def test():
    """Open up a test pcap file and print out the packets"""
    
    pc = pcap.pcap()
    print_packets(pc)



if __name__ == '__main__':
    test()

