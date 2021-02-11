import socket
if __name__ == '__main__':
	try:
		#creating the socket
		server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('socket got created at server end')

		#Binding the socket
		ip_addr='localhost'
		port_no=8989
		address=(ip_addr,port_no)
		server_socket.bind(address)
		print(f'socket got binded to : {ip_addr} running on the port no: {port_no}')

		#making the server socket to listen to the request
		backlog=5
		server_socket.listen(backlog)
		print(f'The server socket can listen to : {backlog} request')

		#accepting the request which came from client and sending the response
		client_access,(ip_addr,port_no)=server_socket.accept()
		print(f'server socket got connected to client socket whose ip address: {ip_addr} running on the port no:{port_no}')
        
        #sending the response to the client
		data='hey client .... thanks for connecting'
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
# server socket got connected to client socket whose ip address: 127.0.0.1 running on the port no:51408
# client access socket got closed

	
