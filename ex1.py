# WAP to create socket and bind that socket to the port number
import socket

if __name__ == '__main__':
					#socket(ipaddress(ipv4),protocol(TCP))
	my_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print('socket created successfully')
	ip_addr='192.168.0.105'  #(or) ip_addr='localhost'
	port_no=8888
	address=(ip_addr,port_no)
	my_sock.bind(address)
	print(f'IP address: {ip_addr}')
	print(f'Port no : {port_no}')
	print(f'socket got binded to : {ip_addr} running on the port no: {port_no}')

# o/p:
# ----
# socket created successfully
# IP address: 192.168.0.105
# Port no : 8888
# socket got binded to : 192.168.0.105 running on the port no: 8888