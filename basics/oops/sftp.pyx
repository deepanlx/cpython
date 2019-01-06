cdef class Base(object):
    cdef:
        str ip, username, password
    def __cinit__(self, ip, username, password):
        print("I am Base class init")
        self.ip = ip
        self.username = username
        self.password = password
        print("I am base class exit")

cdef class SFTP(Base):
    cdef:
        str port
    def __cinit__(self, ip, username, password, port):
        print("SFTP Class Init")
        super(SFTP, self).__init__(ip, username, password)
        self.port = port
        print("SFTP class Exit")

    cdef response(self):
        print("I am from SFTP")

cdef class Server(SFTP):
    #cdef:
    #    str ip, username, password, port
    def __cinit__(self, ip, username, password, port):
        print("Server Class Init")
        super(Server, self).__init__(ip, username, password, port)
        print("Server class Exit")
	
    cdef response(self):
        print("I am from Server entry")
        super(Server, self).response()

if __name__ == "__main__":
    from time import time
    start_time = time()
    server = Server("1.1.1.1", "test", "message", "23")
    server.response()
    end_time = time()
    print(end_time-start_time)
