from tornado.web import RequestHandler
from apps.container import Container

class PingHandler(RequestHandler):
    def get(self):
        self.write('pong')

class PongHandler(RequestHandler):
    def get(self):
        self.write('ping')

class PingApp(Container):

    def routes(self):
        routes = [(r"/ping", PingHandler, "GET"), (r"/pong", PongHandler, "GET")]
        return routes

    def name(self):
        return "PingApp"

app = PingApp()