class Base(object):
	#__slots__ = ["ip", "username", "password", "port"]
	def __init__(self, ip, username, password):
		print("I am Base class init")
		self.ip = ip
		self.username = username
		self.password = password
		print("I am base class exit")

class SFTP(Base):
	#__slots__ = ["ip", "username", "password", "port"]
	def __init__(self, ip, username, password, port):
		print("SFTP Class Init")
		super(SFTP, self).__init__(ip, username, password)
		self.port = port
		print("SFTP class Exit")

	def response(self):
		print("I am from SFTP")

class Server(SFTP):
	def __init__(self, ip, username, password, port):
		print("Server Class Init")
		super(Server, self).__init__(ip, username, password, port)
		print("Server class Exit")

	def response(self):
		print("I am from Server entry")
		super(Server, self).response()

if __name__ == "__main__":
	from time import time
	start_time = time()
	server = Server("1.1.1.1", "test", "message", "23")
	server.response()
	end_time = time()
	print(end_time-start_time)