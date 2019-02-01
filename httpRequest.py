class HttpRequest:
    def __init__(self, data):
        self.method = None
        self.uri = None
        self.http_version = None
        self.headers = {}
        self.parse_request(data)

    def parse_request(self, data):
        request = data.split('/r/n')
        request = request[0]
        self.parse_request_line(request)

    def parse_request_line(self, request_line):
        request = request_line.split(' ')
        self.method = request[0]
        self.uri = request[1]

        if len(request) > 2:
            self.http_version = request[2]
