from http import server


# Class to handle HTTP requests
class StreamingHandler(server.BaseHTTPRequestHandler):
    def create_page(self):
        self.PAGE = """\
                <html>
                <head>
                <title>WOC</title>
                </head>
                <body>
                <p>Hi!</p>
                </body>
                </html>
                """
        self.content = self.PAGE.encode('utf-8')

    def do_GET(self):
        if self.path == '/':
            # Redirect root path to index.html
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            self.create_page()
            # Serve the HTML page
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(self.content))
            self.end_headers()
            self.wfile.write(self.content)
        else:
            # Handle 404 Not Found
            self.send_error(404)
            self.end_headers()
