import socket
if __name__ == '__main__':
	try:
		#creating the socket
		client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('socket got created at client end')

		#establish the connection using connect()
		ip='localhost'
		port=8989
		address=(ip,port)
		client_socket.connect(address)
		print(f'socket got connected to : {ip} running on the port no: {port}')
		print(f'a new connection got established')

		data=input('Enter the msg for server:\t')
		bufsize=1024

		while data!='stop':
			#sending the response to the server
			client_socket.send(data.encode('utf-8'))

			#to recieve the message from the server
			data=client_socket.recv(bufsize).decode('utf-8')
			if not data:
				break

			print(f'The response from server: {data}')
			data=input('Enter the message for server:\t')

	except socket.error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		client_socket.close()
		print('client socket socket got closed')

# o/p:
# -----
# socket got created at client end
# socket got connected to : localhost running on the port no: 8989
# a new connection got established
# Enter the msg for server:       hi server how r u?
# The response from server: im fine client..wt abt u?
# Enter the message for server:   im good...whats up?
# The response from server: nothing
# Enter the message for server:   stop
# client socket socket got closed