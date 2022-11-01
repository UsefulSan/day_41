from flask import request, Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.headers)
    return 'Hello, World!'


@app.route('/json/')
def json():
    return {'json': 42}  # Возвращает тип application/json


@app.route('/html/')
def html():
    return render_template('index.html')  # Возвращает тип text/html


@app.route('/not_found')
def not_found():
    return 'Oops!', 404


@app.route('/foo')
def foo():
    response = make_response('foo')
    # Устанавливаем заголовок
    response.headers['X-Parachutes'] = 'parachutes are cool'
    # Меняем тип ответа
    response.mimetype = 'text/plain'
    # Задаем статус
    response.status_code = 418
    # Устанавливаем cookie
    response.set_cookie('foo', 'bar')
    return response


@app.post('/users')
def users():
    return 'Users', 302
