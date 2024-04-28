from http import server

from weather import sky, webdata


# Class to handle HTTP requests
class StreamingHandler(server.BaseHTTPRequestHandler):
    def create_page(self):
        self.PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <title>Weather Station</title>
    <style>
        /* Basic HTML and body styling */
        body, html {
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #bbafaf; /* Light grey background */
        }

        /* Flexbox setup for center alignment */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Styling for the text container */
        .centered-text {
            background-color: #'''

        if sky == 'sunny':
            self.PAGE += 'f9d835'  # Sunny yellow background
        elif 'rain' in sky:
            self.PAGE += '087c9d'  # Rainy blue background
        elif 'cloud' in sky:
            self.PAGE += '6c6868'  # Cloudy gray background

        self.PAGE += '''; 
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            opacity: 0;
            animation: fadeIn 1.5s ease-out forwards;
            font-family: 'Roboto', sans-serif;
        }
        
        .centered-text p {
            margin: 8px 0;
            font-size: 20px;
            color: #333;
        }
        
        footer {
            position: absolute;
            bottom: 10px;
            left: 10px;
            font-size: 14px;
            color: #666;
            font-family: 'Roboto', sans-serif;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="centered-text">'''

        for line in webdata.splitlines():
            self.PAGE += "<p>" + line + "</p>"

        self.PAGE += '''
    </div>
    <footer>
        &copy; 2024 Neal Team 6. All rights reserved.
    </footer>
</body>
</html>
'''
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
