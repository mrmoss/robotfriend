#!/usr/bin/env python3
'''
Lidar (robot) sender side
'''
import time

import robot_lib

def main():
    '''
    Main
    '''
    # Create a sender socket
    sock = robot_lib.create_tx_socket()

    # Start sending data
    print('transmitting')
    while True:
        print('.', end='', flush=True)
        robot_lib.sock_send_auth(sock, 'imaprettykitty', ['aaa', 'bbb', 'foo', 'bar'])
        time.sleep(1)


if __name__ == '__main__':
    main()
