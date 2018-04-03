import socket 					#imports socket library
import threading				#for multiclient based application multi threads are required

s = socket.socket()         	#Creating an object of the socket class 
port = 12345 					#Port that the socket will bind to
s.bind(('0.0.0.0', port))       #Socket is bound to the port
s.listen(5)						#Can accept upto 5 connections
client_list = []				#will keep a record of all the systems connected to the machine

def new_thread(c):				#Function to be used in Multithreading for many clients
	global client_list
	while True:					#loop through the same client, maintain connection for chat app
		val = c.recv(1024)
		for i in client_list:
			i.send(val)
		print(val)
		
def new_message(c):
	while True:
		a = input()
		global client_list
		for i in client_list:
			i.send(a.encode())

while True:						#accepting multiple clients on this using this loop
	if client_list == []:
		print('Nobody is yet connected on P2P')
	c, addr = s.accept()     	#This will stop execution unless there is a connection request
	c.send('Thank you for connecting'.encode('utf-8'))
	global client_list
	client_list.append(c)
	t1 = threading.Thread(target=new_thread,args=(c,))
	t2 = threading.Thread(target=new_message,args=(c,))
	t2.start()
	t1.start()