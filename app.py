#!/usr/bin/python
 
import SimpleHTTPServer
import SocketServer
 
PORT = 8080
 
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
 
httpd = SocketServer.TCPServer(("", PORT), Handler)
 
print "Hello World, serving at port", PORT
httpd.serve_forever()
