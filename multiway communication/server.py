import socket
if __name__ == '__main__':
	try:
		#creating the socket
		server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('socket got created at server end')

		#Binding the socket
		ip='localhost'
		port=8989
		address=(ip,port)
		server_socket.bind(address)
		print(f'socket got binded to : {ip} running on the port no: {port}')

		#making the server socket to listen to the request
		backlog=5
		server_socket.listen(backlog)
		print(f'The server socket can listen to : {backlog} request')

		#accepting the request and message which came from client 
		client_access,(ip_client,port_client)=server_socket.accept()
		print(f'server socket got connected to client whose ip address : {ip_client} running on the port no: {port_client}')
		
		bufsize=1024
		while True:
			#collecting the message from client
			data=client_access.recv(bufsize).decode('utf-8')

			if not data:
				break

			print(f'The message from client: {data}')

			#sending the message to the client
			data=input('Enter the msg for client:\t')
			client_access.send(data.encode('utf-8'))

	except socket.error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		client_access.close()
		print('client access socket got closed')

# o/p:
# ----
# socket got created at server end
# socket got binded to : localhost running on the port no: 8989
# The server socket can listen to : 5 request
# server socket got connected to client whose ip address : 127.0.0.1 running on the port no: 52739
# The message from client: hi server how r u?
# Enter the msg for client:       im fine client..wt abt u?
# The message from client: im good...whats up?
# Enter the msg for client:       nothing
# client access socket got closed