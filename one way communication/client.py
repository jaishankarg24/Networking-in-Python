import socket
if __name__ == '__main__':
	try:
		#creating the socket
		client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('socket got created at client end')

		#establish the connection using connect()
		ip_addr='localhost'
		port_no=8989
		address=(ip_addr,port_no)
		client_socket.connect(address)
		print(f'socket got connected to : {ip_addr} running on the port no: {port_no}')
		print(f'a new connection got established')
        
        #to recieve the response from the server
		bufsize=1024
		recv_data=client_socket.recv(bufsize).decode('utf-8')
		print(f'The response from server: {recv_data}')
	except socket.error as msg:
		print(f'The cause of the exception : {msg}')
	finally:
		client_socket.close()
		print('client socket socket got closed')

# o/p:
# ----
# socket got created at client end
# socket got connected to : localhost running on the port no: 8989
# a new connection got established
# The response from server: hey client .... thanks for connecting
# client socket socket got closed