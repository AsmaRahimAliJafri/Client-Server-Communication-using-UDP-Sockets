import socket


UDP_IP_ADDRESS_sensor = "192.168.56.1"
UDP_IP_ADDRESS_server = "192.168.56.1"
UDP_PORT_NO_sensor = 6789
UDP_PORT_NO_server = 6780

#creating sockets
clientSock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#code that recieves messages from the udp sensor
clientSock1.bind((UDP_IP_ADDRESS_sensor, UDP_PORT_NO_sensor))

avg =0
#operating and printing the data
while True:
    data, addr = clientSock1.recvfrom(1024)
    got = int(data)
    var_to_serv = got*2
    print("Message  ", var_to_serv)
    avg += var_to_serv
    if var_to_serv == 0:
       break


#code that sends the udp msg
final_avg = avg/5
#print("Average  ", final_avg)
float_to_str = str(final_avg)
str_encode = float_to_str.encode()

clientSock2.sendto(str_encode, (UDP_IP_ADDRESS_server, UDP_PORT_NO_server))
