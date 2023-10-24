# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
import subprocess
import sys
import logging

hostName = "192.168.8.143"
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        #os.system('python main.py grape_helth.JPG')
        #exec(p2)
        #result = subprocess.run(["python", "main.py","grape_helth.JPG"], capture_output=True, text=True)
        #print(result.stdout)

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        str(self.path), str(self.headers), post_data.decode('utf-8'))
        result = subprocess.run(["python", "main.py",post_data], capture_output=True, text=True)
        print(result.stdout)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(result.stdout.format(self.path).encode('utf-8'))


    #

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

