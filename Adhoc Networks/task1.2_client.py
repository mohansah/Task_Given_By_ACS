import socket 	# Import socket module
import sys  	# Import sys module
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	# Create a socket object
    print("Socket successfully created")
except socket.error as err: 
    print("socket creation failed with error %s" %(err))
  
port = 12345		# Define the port on which you want to connect

host_name=socket.gethostname()		# for getting the host name
host_ip=socket.gethostbyname(host_name)	# for getting the host ip address

s.connect((host_ip, port))	# connect to the server on local computer

s.send(bytes(input("Enter Email id : "), 'utf-8'))	# send email id entered by the user to the server

if str(s.recv(100),"utf-8")=="True":
    s.send(bytes(input("Enter Password : "), 'utf-8'))    # send password entered by the user to the server 
    msg=s.recv(100)	# receive data from the server 
    print("Message from server: "+str(msg,"utf-8"))
else:
    print("No account with this email")

s.close()		# close the connection
