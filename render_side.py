#!/usr/bin/env python3
'''
Render (human) receiver side
'''
import time

import robot_lib

def main():
    '''
    Main
    '''
    # Create a receiver socket
    sock = robot_lib.create_rx_socket()

    # Start receiving data
    print('listening')
    while True:
        if robot_lib.sock_has_data(sock):
            payload = robot_lib.sock_recv_auth(sock, 'imaprettykitty')
            print(payload)
        print('.', end='', flush=True)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
