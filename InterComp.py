from socket import *

s = socket()

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.con = None
        
        s.bind((host, port))
        s.listen(5)

    def connect(self):
        conn, addr = s.accept()
        self.con = conn

        return {'address': addr, 'conn_id': conn}

    def recieve(self):
        con = self.con
        return con.recv(4096).decode()

    def close(self):
        con = self.con
        con.close()

    def send(self, data):
        con = self.con
        con.send(bytes(data, 'utf-8'))


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        s.connect((host, port))

    def recv(self):
        return s.recv(4096).decode()

    def send(self, Data):
        s.send(bytes(Data, 'utf-8'))


