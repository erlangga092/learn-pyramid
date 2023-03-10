from pyramid.config import Configurator
from pyramid.response import Response
from wsgiref.simple_server import make_server


def hello_world(request):
    print("Incoming request")
    return Response("<body><h1>Hello World!</h1></body>")


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("hello", "/")
        config.add_view(hello_world, route_name="hello")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 6543, app)
    server.serve_forever()
