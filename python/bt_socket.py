import socket


bluetoothAddress = "c0-e4-34-1c-8b-04" #The machines bluetooth adapter's MAC address
port = 3
backlog = 1
size = 1024

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) #init the socket to use bluetooth
s.bind((bluetoothAddress, port))
s.listen(backlog)

while 1:
    
