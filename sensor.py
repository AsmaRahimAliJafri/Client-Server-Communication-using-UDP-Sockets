import socket

UDP_IP_ADDRESS = "192.168.56.1"
UDP_PORT_NO =6789
x=0

#creating sockets
sensorSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#code that sends the udp msg

num = [1, 2, 3, 4, 5,0]
length_of_list = len(num)


while (x < 6):
        string_to_client = str(num[x])
        byte_to_client = string_to_client.encode()
        sensorSock.sendto(byte_to_client, (UDP_IP_ADDRESS, UDP_PORT_NO))
        x = x+1


