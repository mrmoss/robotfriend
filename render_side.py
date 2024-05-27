#!/usr/bin/env python3
import socket
import struct
import time

import robot_lib

def main():
    # Create a receiver socket
    sock = robot_lib.create_rx_socket()

    print('listening')
    while True:
       # if robot_lib.is_data_ready(sock):
        data = sock.recv(10240)
        print(data)
        # print('.', end='')
        #time.sleep(0.1)

if __name__ == '__main__':
    main()
