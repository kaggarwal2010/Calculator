import os,sys
from http.server import CGIHTTPRequestHandler, HTTPServer

webdir = '.'
port = 9000

os.chdir(webdir)
server_address = ("", port)
srvrobj = HTTPServer(server_address, CGIHTTPRequestHandler)
srvrobj.serve_forever()
