'''
Helper library for robot stuff
'''
import select
import socket
import struct

# Use this address and port for a UDP multicast group (note: this is not your ip address)
MULTICAST_GROUP_ADDR = '224.1.1.1'
MULTICAST_GROUP_PORT = 42069
multicast_group = (MULTICAST_GROUP_ADDR, MULTICAST_GROUP_PORT)


def create_tx_socket():
    '''
    Returns a socket object that's been setup for sending data
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # There's a timeout when reusing the same addr+port, we're going to disable it
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Multicast mode (TTL is 2 seconds)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    # Return socket for use
    return sock


def create_rx_socket():
    '''
    Returns a socket object that's been setup for receiving data
    '''
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # Bind to the addr+port we'll be listening to
    sock.bind(multicast_group)

    # Create a membership struct and apply said membership to our socket
    mreq = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP_ADDR), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Return socket for use
    return sock


def sock_has_data(sock):
    '''
    Checks if a socket has data that can be read on it
    '''
    readable, _writeable, _errored = select.select([sock], [], [], 0)
    return sock in readable
