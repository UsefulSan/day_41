from wsgiref.simple_server import make_server
from example import app


def server(wsgi_app):
    serverd = make_server('', 5000, wsgi_app)
    print("Serving HTTP on port 5000...")
    serverd.serve_forever()


if __name__ == '__main__':
    app.run(debug=True)
