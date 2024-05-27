import socket
import struct

multicast_group_addr = '224.1.1.1'
multicast_group_port = 42069

multicast_group = (multicast_group_addr, multicast_group_port)

def create_tx_socket():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    
    # There's a timeout when reusing the same addr+port, we're going to disable it
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Multicast mode (TTL is 2 seconds)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    # Return socket for use
    return sock

def create_rx_socket():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    
    # Bind to the addr+port we'll be listening to
    sock.bind(multicast_group)

    # Create a membership struct and apply said membership to our socket
    mreq = struct.pack("4sl", socket.inet_aton(multicast_group_addr), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Return socket for use
    return sock

def is_data_ready(sock):
    try:
        readable, writeable, errored = select.select([sock], [], [], 0)
        if sock in readable:
            return True
    except Exception:
        pass
    return False