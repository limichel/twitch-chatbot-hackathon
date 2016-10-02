import socket

class Socket:
	def __init__(self):
		'''Initializes a new socket with a read file and a write file'''
		self.socket = socket.socket() # Creates a socket
		self.input = self.socket.makefile('r') # Creates a file where we read outputs from the server
		self.output = self.socket.makefile('w') # Creates a file where we write inputs to the client

	def close_socket(self):
		''' Closes the socket and its associated read and write files'''
		self.input.close()
		self.output.close()
		self.socket.close()

	def send_message(self, message: str):
		'''Writes a message to the connected server'''
		self.output.write(message + '\r\n')
		self.output.flush()

	def receive_response(self):
		'''Receives a response from the connected server'''
		response = ''
		for line in self.input:
			print('hi')
			response += line
			if 'End of /NAMES list' in line:
				break
		return response if response != '' else None
		
	def connect(self, host: str, port: int):
		self.socket.connect((host, port))