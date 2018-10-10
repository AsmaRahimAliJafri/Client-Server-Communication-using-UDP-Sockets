import socket

UDP_IP_ADDRESS = "192.168.56.1"
UDP_PORT_NO = 6780

#creating server socket which listens for udp mgsgs
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#binding the newly created socket to the ip and the port no
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

#WHILE LOOPS KEEPS LISTENING TO SOCKET UNTIL TERMINATION
while True:
    data, addr = serverSock.recvfrom(1024)
    print "Message: ", data