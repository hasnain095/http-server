from tcpHandler import TCPHandler


class HttpServer(TCPHandler):
    headers = [
        'Server: StaticFileServer',
        'Content-Type: text/html',
    ]

    status_codes = {
        '200': 'OK',
        '404': 'Not Found',
    }

    def handle_request(self, data):
        response = (
            b'HTTP/1.1 200 OK\r\n',
            b'Server: StaticFileServer\r\n',
            b'Content-Type: text/html\r\n',
            b'\r\n',
            b'<html><body><h1>Hello World</h1></body></html>'
        )
        return b"".join(response)

    def response(self, status_code):
        response_detail = self.status_codes[status_code]
        return b'HTTP/1.1 {} {}\r\n'.format(status_code, response_detail)

    def headers(self):
        response = b''
        for header in self.headers:
            response += b'{}'.format(header)

        return response
