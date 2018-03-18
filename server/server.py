import socket
import os
import time
from multiprocessing import Process



def f(x):
	time.sleep(5)
	
	print (x)

if __name__ == "__main__":

	x = {
	"1": 2,
	"3": 4,
	"5": 6
	}
	p = Process(target = f, args = (x, ))
	p.start()
	x["6"] = 8
	
	p.join()
	'''
	port = 8888
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("localhost", port))
	server.listen(0)

	while True:
		print ("lalala")
		connection, address = server.accept()
		connection.send(bytes("test: {}".format(connection.recv(1024).decode('utf-8')), 'utf-8'))
	connection.close()
	'''