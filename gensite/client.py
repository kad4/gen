# This is client.py file
import socket
import pickle
from sys import getsizeof

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port=6200

s.connect(('127.0.0.1', port))

data={'action':'login'}
b = pickle.dumps(data,protocol=pickle.HIGHEST_PROTOCOL)
s.send(b)

buff= pickle.loads(s.recv(1024))
print (pickle.loads(s.recv(buff)))
s.close()
# Close the socket when done