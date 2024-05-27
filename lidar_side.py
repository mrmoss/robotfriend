#!/usr/bin/env python3
import socket
import struct
import time

import robot_lib

def main():
    # Create a sender socket
    sock = robot_lib.create_tx_socket()
    
    print('transmitting')
    while True:
        sock.sendto(b"robot", robot_lib.multicast_group)
        time.sleep(1)

if __name__ == '__main__':
    main()