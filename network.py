import socket
import pickle

class NetWork:

    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server = "192.168.1.6"
        self._port = 5555
        self._addr = (self._server, self._port)
        self._p = self.connect()
        #print(self._id)
    
    def get_p(self):
        return self._p

    def connect(self):
        try:
            self._client.connect(self._addr)
            return pickle.loads(self._client.recv(2048))
        except:
            pass
    
    def send(self, data):
        try:
            self._client.send(pickle.dumps(data))
            return pickle.loads(self._client.recv(2048))
        except socket.error as e:
            print(e)

# Testing network socket 
""" 
network = NetWork()
print(network.send("hello"))
print(network.send("working")) 
"""