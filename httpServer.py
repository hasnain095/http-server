from socket import socket

class HttpServerTCPHandler(socketserver.BaseRequestHandler):
    def __init__(self):
        self.host = "localhost"
        self.port = 9999


    def start(self):
        self.server_socket = socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_STREAM, socket.SO_REUSERADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        print("Listening at {} {}".format(self.host, self.port))

        while True:
            client_conn, client_addr = self.server_socket.accept()
            print("Connected to {}".format(client_addr))
            data = client_conn.recv(4096)

            response = self.handle_request(data)

            client_conn.sendall(response)
            client_conn.close()


    def handle_request(self):
        while True:


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
