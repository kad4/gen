import socket
import pickle
import json
from sys import getsizeof
from serverConfig import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

print("Port established. Awating connection.")
c = None
while True:
    try:
        output = None
        c, addr = s.accept()

        print("Connection established with ", addr)

        request = json.loads(c.recv(1024).decode())

        print("Incoming request : ", request)

        print(request["action"])
        if request["action"] == "login":
            print(request["username"], " ", request["password"])
            if request["username"] == "aayush" and request["password"] == "subedi":
                output = [True, 451]
            else:
                output = [False]
        elif request["action"] == "like" or request["action"] == "logout":
            pass
        elif request["action"] == "checkSession":
            print(request["id"])
            if request["id"] == 451:
                output = [True]
            else:
                output = [False]
        elif request["action"] == "retrievePost":
            posts = [{"title": request["type"] + " " + str(i), "id":i, "url":'http://'+host, "state": i % 3} for i in range(10)]
            output = posts
        elif request["action"] == "retrieveContent":
            output = "<h1><p>Content for post " + str(request["id"]) + "</p></h1>"
        else:
            pass

        if output is not None:
            print("Pushing output : ", output)
            output = json.dumps(output)
            outputBufferSize = getsizeof(output)

            print("Buffer size : ", outputBufferSize)
            c.send(pickle.dumps(outputBufferSize, protocol=0))
            c.send(output.encode())

        print("Data transmission successful.")

        c.close()
        print("Connection with ", addr, " terminated.")
    except Exception as e:
        try:
            c.close()
        except:
            pass
        print(e)
