import socket


class TCPHandler:
    """
    This class manages the tcp connection, creation of socket, and listening for connection
    """

    def __init__(self):
        self.host = "localhost"
        self.port = 9999

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

    def handle_request(self, data):
        """
        Processes the request and returns response
        """
        return data
