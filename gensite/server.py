# This is server.py file
import socket
import pickle
from sys import getsizeof

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6201
s.bind(('127.0.0.1', port))
s.listen(5)

# while True:
c, addr = s.accept()
request = pickle.loads(c.recv(1024))

# pickle_data=None
pickle_data = pickle.dumps('hail hydra')
c.send(pickle.dumps(getsizeof(pickle_data)))

if(request['action'] == 'login'):
    print('received')
    c.send(pickle_data)

elif(request['action'] == 'login'):
    pass

c.close()
