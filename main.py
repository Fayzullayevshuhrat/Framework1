from wsgiref.simple_server import  make_server
from app import FrameworkApp

app = FrameworkApp()

server = make_server("localhost",8000, app)
server.serve_forever()