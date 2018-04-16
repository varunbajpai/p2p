import socket               
import threading

s = socket.socket()         
port = 12345
s.connect(('127.0.0.1', port))
print(s.recv(1024))
one_time = 1

def reception(c):
	while True:
		save_data = c.recv(200000)
		print(save_data)
		f = open('file_path.txt','ab+')
		f.write(save_data)
		f.close()

def sending(c):
	while True:
		a = input()
		c.send(a.encode())
	
while True:
	if one_time == 1:
		t1 = threading.Thread(target=reception,args=(s,))
		t2 = threading.Thread(target=sending,args=(s,))
		t1.start()
		t2.start()
		one_time = 2
	
s.close() 