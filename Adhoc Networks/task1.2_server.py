import socket       		# Import socket module
import sys  			# Import sys module

try:         
    s = socket.socket()           	# Create a socket object
    print("Socket successfully created")
except socket.error as err: 
    print("socket creation failed with error %s" %(err))

port = 12345		# Define the port on which you want to connect

host_name=socket.gethostname()		# for getting the host name
host_ip=socket.gethostbyname(host_name)	# for getting the host ip address
              
s.bind((host_ip, port))    # binding to the port
s.listen(5)    		   # put the socket into listening mode   
print("socket is listening")           

# record of email is and password
dist={'radhemohan1001001@gmail.com':'12345','mohan@gmail.com':'98765','sohan@gmail.com':'123456789'}

while True:  
    c, addr = s.accept() 		# Establish connection with client.     
    print('Got connection from', addr)
    data=c.recv(1024)		# receive data from the client

    for email in dist.keys():		# for verifying the email is present in our record or not
        if str(data,"utf-8")==email:
            c.send(bytes("True", 'utf-8'))	 # send True message to the client.  
            data1=c.recv(1024)		# receive data from the client
            if str(data1,"utf-8")==dist[email]:     # for verifying the password
                c.send(bytes("Connection Successful", 'utf-8'))		# send Connection Successful message to the client.  
            else:
                c.send(bytes("Connection Fail : Wrong Password", 'utf-8'))		# send Wrong Password message to the client.  
            break

    c.close()		# close the connection
