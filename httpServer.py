import os
from http.client import responses as HTTP_RESPONSES
from tcpHandler import TCPHandler
from httpRequest import HttpRequest


class HttpServer(TCPHandler):
    headers = [
        'Server: StaticFileServer',
        'Content-Type: text/html',
    ]

    status_codes = HTTP_RESPONSES

    def handle_request(self, data):

        request = HttpRequest(data.decode())

        try:
            handler = getattr(self, "handle_%s" % request.method)
        except AttributeError:
            handler = self.HTTP_501_handler()

        response = handler(request)

        # response_line = self.response_line(200)
        # response_headers = self.response_headers()
        # blank_line = '\r\n'
        # response_body = "<html><body><h1>Hello World</h1></body></html>"

        # response = "%s%s%s%s" % (response_line, response_headers, blank_line, response_body)
        return response.encode()

    def response_line(self, status_code):
        response_detail = self.status_codes[status_code]
        return 'HTTP/1.1 %d %s\r\n' % (status_code, response_detail)

    def response_headers(self, extra_headers=None):
        headers = self.headers.copy()
        if extra_headers:
            headers += extra_headers
        response = ''
        for header in headers:
            response += '%s\r\n' % header

        return response

    def handle_OPTIONS(self, request):
        response_line = self.response_line(200)

        extra_header = ["Allow: OPTIONS, GET"]
        response_header = self.response_headers(extra_header)
        blank_line = "\r\n"

        return "%s%s%s" % (response_line, response_header, blank_line)

    def handle_GET(self, request):
        filename = request.uri.strip('/')

        if os.path.exists(filename):

            response_line = self.response_line(200)
            response_headers = self.response_headers()
            blank_line = '\r\n'
            with open(filename) as file:
                    response_body = file.read()

        else:
            return self.HTTP_404_handler(request)

        response = "%s%s%s%s" % (response_line, response_headers, blank_line, response_body)

        return response

    def HTTP_501_handler(self, request):
        response_line = self.response_line(501)
        response_headers = self.response_header()
        blank_line = "\r\n"
        response_body = "<html><h1> 501: Not Implemented</h1></html>"

        return "%s%s%s%s" % (response_line, response_headers, blank_line, response_body)

    def HTTP_404_handler(self, request):
        response_line = self.response_line(404)
        response_headers = self.response_headers()
        blank_line = "\r\n"

        response_body = "<html><h1> 404: Not Found</h1></html>"

        return "%s%s%s%s" % (response_line, response_headers, blank_line, response_body)
