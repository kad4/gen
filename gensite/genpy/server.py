import socket
import pickle
from sys import getsizeof
from serverConfig import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()

    request = pickle.loads(c.recv(1024))

    if request['action'] is 'login':
        if request['username'] is 'aayush' and request['password'] is 'subedi':
            output = [True, 451]
        else:
            output = [False]
    elif request['action'] is 'like':
        pass
    elif request['action'] is 'checkSession':
        if request['id'] is 451:
            output = [True]
        else:
            output = [False]
    elif request['action'] is 'retrievePost':
        posts = [{'title': request['type'] + ' ' + str(i), 'id':i, 'url':host, 'state': i % 3} for i in range(10)]
        output = posts
    elif request['action'] is 'retrieveContent':
        output = 'Content for post ' + str(request['id'])

    output = pickle.dumps(output)

    c.send(getsizeof(output))
    c.send(output)

    c.close()
